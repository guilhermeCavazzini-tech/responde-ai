from google.adk.agents import Agent
from resolveai.utils.model import MODEL_CONFIG
from .tools import manage_pending_issues
from .prompt import prompt

management_agent = Agent(
    name="management_agent",
    model=MODEL_CONFIG["light"],
    description="Agente para gestão de pendências e priorização",
    instruction=(prompt),
    tools=[manage_pending_issues]
)