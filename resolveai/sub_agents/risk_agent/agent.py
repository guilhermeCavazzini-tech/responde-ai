from .tools import assess_risk
from google.adk.agents import Agent
from resolveai.utils.model import MODEL_CONFIG

risk_agent = Agent(
    name="risk_agent",
    model=MODEL_CONFIG["light"],
    description="Agente para avaliação de riscos aos cidadãos",
    instruction="Classifique o nível de perigo de problemas urbanos e recomende ações de mitigação",
    tools=[assess_risk]
)
