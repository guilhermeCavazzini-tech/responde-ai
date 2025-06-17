from typing import Optional

# Agente Detector de Problemas
def detect_urban_issues(location: str, issue_type: Optional[str] = None) -> dict:
    """Detecta problemas urbanos como buracos, vazamentos ou fios caídos.
    
    Args:
        location (str): Localização do problema (endereço ou coordenadas)
        issue_type (str, optional): Tipo específico de problema a ser verificado
        
    Returns:
        dict: status e relatório ou mensagem de erro
    """
    # Simulação - em produção integraria com APIs de geolocalização e image recognition
    issues_db = {
        "Central Park": ["buraco no asfalto", "lâmpada queimada"],
        "5th Avenue": ["vazamento de água"],
        "Broadway": ["fio elétrico caído"]
    }
    
    if location in issues_db:
        if issue_type:
            issues = [issue for issue in issues_db[location] if issue_type in issue]
        else:
            issues = issues_db[location]
        
        if issues:
            return {
                "status": "success",
                "issues": issues,
                "count": len(issues),
                "location": location
            }
    
    return {
        "status": "error" if issue_type else "success",
        "message": f"Nenhum {issue_type if issue_type else 'problema'} encontrado em {location}",
        "issues": [] if not issue_type else None
    }
