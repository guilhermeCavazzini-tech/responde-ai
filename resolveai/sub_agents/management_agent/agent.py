from google.adk.agents import Agent
from resolveai.utils.model import MODEL_CONFIG
from .tools import manage_pending_issues

management_agent = Agent(
    name="management_agent",
    model=MODEL_CONFIG["light"],
    description="Agente para gestão de pendências e priorização",
    instruction="Gerencie eficientemente o fluxo de trabalho de resolução de problemas baseado em prioridades",
    tools=[manage_pending_issues]
)