import os
from moya.agents.base_agent import AgentConfig
from moya.agents.ollama_agent import OllamaAgent
from moya.classifiers.llm_classifier import LLMClassifier
from moya.orchestrators.multi_agent_orchestrator import MultiAgentOrchestrator
from moya.registry.agent_registry import AgentRegistry
from moya.tools.ephemeral_memory import EphemeralMemory
from moya.tools.tool_registry import ToolRegistry


def setup_memory_components():
    """Set up memory components for the agents."""
    tool_registry = ToolRegistry()
    EphemeralMemory.configure_memory_tools(tool_registry)
    return tool_registry


def create_technical_agent(tool_registry):
    """Create a technical Ollama agent using local Mistral model."""
    agent_config = AgentConfig(
        agent_name="technical_agent",
        agent_type="ChatAgent",
        description="Technical specialist using Ollama Mistral model",
        system_prompt="You are a helpful technical assistant.",
        llm_config={
            "base_url": "http://localhost:11434",  # Ollama local API
            "model_name": "mistral",
        },
        tool_registry=tool_registry,
    )
    return OllamaAgent(agent_config)


def create_classifier_agent():
    """Create a classifier agent for routing messages."""
    classifier_prompt = """You are a classifier. Your job is to determine the best agent based on the user's message:
1. If the message is technical, route to 'technical_agent'
2. Otherwise, route to 'default_agent'

Return only the agent name."""

    classifier_config = AgentConfig(
        agent_name="classifier",
        agent_type="AgentClassifier",
        description="Routes messages to agents based on keywords",
        system_prompt=classifier_prompt,
        llm_config={
            "base_url": "http://localhost:11434",
            "model_name": "mistral",
        },
    )
    return OllamaAgent(classifier_config)


def setup_orchestrator():
    """Set up the multi-agent orchestrator with all components."""
    tool_registry = setup_memory_components()

    technical_agent = create_technical_agent(tool_registry)
    classifier_agent = create_classifier_agent()

    registry = AgentRegistry()
    registry.register_agent(technical_agent)

    classifier = LLMClassifier(classifier_agent, default_agent="technical_agent")

    orchestrator = MultiAgentOrchestrator(
        agent_registry=registry,
        classifier=classifier,
        default_agent_name="technical_agent",
    )

    return orchestrator
