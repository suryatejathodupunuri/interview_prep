from moya.agents.base_agent import AgentConfig
from agents.ollama_agent import OllamaAgent

def create_behavioral_agent():
    config = AgentConfig(
        agent_name="behavioral_agent",
        agent_type="OllamaAgent",
        description="Handles behavioral interview questions based on past interactions.",
        system_prompt="You are a behavioral interview expert who remembers past sessions.",
        llm_config={
            "base_url": "http://localhost:11434",
            "model_name": "mistral"
        }
    )
    return OllamaAgent(agent_config=config)
