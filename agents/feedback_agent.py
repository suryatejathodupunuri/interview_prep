from moya.agents.base_agent import AgentConfig
from agents.ollama_agent import OllamaAgent

def create_feedback_agent():
    config = AgentConfig(
        agent_name="feedback_agent",
        agent_type="OllamaAgent",
        description="Provides semantic skill feedback and tracks progress.",
        system_prompt="You provide constructive feedback on interview skills.",
        llm_config={
            "base_url": "http://localhost:11434",
            "model_name": "mistral"
        }
    )
    return OllamaAgent(agent_config=config)
