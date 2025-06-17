from resolveai.sub_agents.analysis_agent import analysis_agent
from resolveai.sub_agents.detection_agent import detection_agent
from resolveai.sub_agents.management_agent import management_agent
from resolveai.sub_agents.registration_agent import registration_agent
from resolveai.sub_agents.risk_agent import risk_agent

from .prompt import prompt 

from typing import Dict
from google.adk.agents import Agent
from resolveai.utils.model import MODEL_CONFIG



# Agente Supervisor (Gestor)
def supervise_agents(agent_reports: Dict[str, dict]) -> dict:
    """Supervisiona o status de todos os agentes e coordena ações.
    
    Args:
        agent_reports (Dict[str, dict]): Relatórios de status dos agentes
        
    Returns:
        dict: status geral e recomendações
    """
    overall_status = "operational"
    issues_detected = 0
    high_priority = 0
    
    for agent, report in agent_reports.items():
        if report.get("status") != "success":
            overall_status = "partial_outage"
        if "issues" in report and report["issues"]:
            issues_detected += len(report["issues"])
        if "risk_assessment" in report and report["risk_assessment"]["level"] == "critical":
            high_priority += 1
    
    if high_priority > 0 or overall_status == "partial_outage":
        overall_status = "critical_attention_needed"
    
    return {
        "status": "success",
        "supervision_report": {
            "system_status": overall_status,
            "total_issues_detected": issues_detected,
            "high_priority_issues": high_priority,
            "recommendation": "Expandir equipe de reparos" if high_priority > 2 else "Manter operação normal"
        }
    }



# Agente Supervisor Principal
root_agent = Agent(
    name="urban_management_supervisor",
    model=MODEL_CONFIG["light"],
    description="Agente supervisor para coordenação de todos os agentes de gestão urbana",
    instruction=(prompt),
    tools=[supervise_agents],
    sub_agents=[detection_agent, risk_agent, registration_agent, analysis_agent, management_agent]
)