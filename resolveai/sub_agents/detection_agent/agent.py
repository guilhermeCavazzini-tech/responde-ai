from google.adk.agents import Agent
from resolveai.utils.model import MODEL_CONFIG
from .tools import detect_urban_issues

detection_agent = Agent(
    name="detection_agent",
    model=MODEL_CONFIG["light"],
    description="Agente para detecção de problemas urbanos como buracos, vazamentos e fios caídos",
    instruction="Analise relatos e imagens para identificar problemas de infraestrutura urbana com precisão",
    tools=[detect_urban_issues]
)
