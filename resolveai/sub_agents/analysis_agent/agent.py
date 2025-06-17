from google.adk.agents import Agent
from resolveai.utils.model import MODEL_CONFIG
from .tools import analyze_issues
from .prompt import prompt

analysis_agent = Agent(
    name="analysis_agent",
    model=MODEL_CONFIG["light"],
    description="Agente para análise de dados de problemas urbanos",
    instruction= (prompt),
    tools=[analyze_issues]
)
