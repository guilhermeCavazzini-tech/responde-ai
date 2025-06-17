from .tools import assess_risk
from google.adk.agents import Agent
from resolveai.utils.model import MODEL_CONFIG
from .prompt import prompt

risk_agent = Agent(
    name="risk_agent",
    model=MODEL_CONFIG["light"],
    description="Agente para avaliação de riscos aos cidadãos",
    instruction=(prompt),
    tools=[assess_risk]
)
