# Agente de Gerenciamento de Riscos
def assess_risk(issue_description: str) -> dict:
    """Avalia o nível de risco de um problema detectado para humanos.
    
    Args:
        issue_description (str): Descrição do problema detectado
        
    Returns:
        dict: classificação de risco e recomendações
    """
    risk_levels = {
        "buraco no asfalto": {"level": "medium", "action": "Sinalizar área"},
        "vazamento de água": {"level": "high", "action": "Isolar área e notificar concessionária"},
        "fio elétrico caído": {"level": "critical", "action": "Isolar imediatamente e chamar equipe especializada"},
        "lâmpada queimada": {"level": "low", "action": "Substituir na próxima manutenção"}
    }
    
    for pattern, data in risk_levels.items():
        if pattern in issue_description.lower():
            return {
                "status": "success",
                "risk_assessment": {
                    "level": data["level"],
                    "recommended_action": data["action"],
                    "issue": pattern
                }
            }
    
    return {
        "status": "error",
        "message": f"Não foi possível classificar o risco para: {issue_description}"
    }

