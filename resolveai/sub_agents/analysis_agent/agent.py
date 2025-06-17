from google.adk.agents import Agent
from resolveai.utils.model import MODEL_CONFIG
from .tools import analyze_issues

analysis_agent = Agent(
    name="analysis_agent",
    model=MODEL_CONFIG["light"],
    description="Agente para análise de dados de problemas urbanos",
    instruction="Analise padrões e tendências em problemas reportados para identificar áreas críticas",
    tools=[analyze_issues]
)
