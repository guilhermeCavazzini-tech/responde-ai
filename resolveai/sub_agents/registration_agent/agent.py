from .tools import register_issue
from google.adk.agents import Agent
from resolveai.utils.model import MODEL_CONFIG

registration_agent = Agent(
    name="registration_agent",
    model=MODEL_CONFIG["light"],
    description="Agente para cadastro e registro de problemas",
    instruction="Registre meticulosamente cada problema reportado com todos os detalhes necessários",
    tools=[register_issue]
)