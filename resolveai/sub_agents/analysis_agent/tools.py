from typing import Optional

# Agente de Análise de Dados
def analyze_issues(period_days: int = 30, location: Optional[str] = None) -> dict:
    """Analisa problemas reportados por período e localização.
    
    Args:
        period_days (int): Período de análise em dias
        location (str, optional): Filtro por localização
        
    Returns:
        dict: status e resultados da análise
    """
    # Simulação - em produção usaria dados reais
    analysis = {
        "total_issues": 42,
        "by_type": {
            "buraco no asfalto": 15,
            "vazamento de água": 8,
            "fio elétrico caído": 3,
            "outros": 16
        },
        "resolution_rate": 0.65,
        "avg_resolution_time": "2.5 dias"
    }
    
    if location:
        analysis["location_filter"] = location
        analysis["total_issues"] = 12
        analysis["by_type"] = {
            "buraco no asfalto": 5,
            "vazamento de água": 2,
            "outros": 5
        }
    
    return {
        "status": "success",
        "period_days": period_days,
        "analysis": analysis
    }