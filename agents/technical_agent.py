from moya.agents.base_agent import AgentConfig
from agents.ollama_agent import OllamaAgent  # your OllamaAgent implementation

def create_technical_agent():
    config = AgentConfig(
        agent_name="technical_agent",
        agent_type="OllamaAgent",
        description="Handles technical interview questions",
        system_prompt="You are a helpful technical interviewer.",
        llm_config={
            "base_url": "http://localhost:11434",
            "model_name": "mistral"
        }
    )
    return OllamaAgent(agent_config=config)
