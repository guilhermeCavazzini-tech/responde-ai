import datetime
from typing import Optional

# Agente de Cadastro e Registro
def register_issue(location: str, issue_type: str, description: str, reporter: Optional[str] = None) -> dict:
    """Registra um novo problema no sistema de gestão urbana.
    
    Args:
        location (str): Localização do problema
        issue_type (str): Tipo do problema (ex: "buraco no asfalto", "vazamento")
        description (str): Descrição detalhada do problema
        reporter (str, optional): Nome/ID de quem reportou o problema
            
    Returns:
        dict: status e informações do registro
    """
    # Criar estrutura de dados do problema
    issue_data = {
        "location": location,
        "issue_type": issue_type, 
        "description": description,
        "reporter": reporter
    }
    # Simulação - em produção integraria com banco de dados
    timestamp = datetime.datetime.now().isoformat()
    issue_id = f"ISSUE-{hash(f'{timestamp}{issue_data['location']}')}"
    
    return {
        "status": "success",
        "registration": {
            "issue_id": issue_id,
            "timestamp": timestamp,
            **issue_data
        }
    }
