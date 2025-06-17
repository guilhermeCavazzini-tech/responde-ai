"""
Configurações para gerenciar a cota da API Gemini e otimizar o uso dos modelos.
"""

# Configuração de modelos por prioridade de consumo de cota
QUOTA_EFFICIENT_MODELS = {
    "ultra_light": "gemini-1.0-pro",      # Modelo mais antigo, menos consumo
    "light": "gemini-1.5-flash",         # Modelo rápido e econômico
    "standard": "gemini-1.5-pro",        # Modelo padrão
}

# Configuração atual recomendada para plano gratuito
CURRENT_MODEL_CONFIG = {
    "detection": QUOTA_EFFICIENT_MODELS["light"],
    "risk_assessment": QUOTA_EFFICIENT_MODELS["light"], 
    "registration": QUOTA_EFFICIENT_MODELS["light"],
    "analysis": QUOTA_EFFICIENT_MODELS["light"],
    "management": QUOTA_EFFICIENT_MODELS["light"],
    "supervisor": QUOTA_EFFICIENT_MODELS["light"]
}

# Limites aproximados para plano gratuito (por dia)
GEMINI_FREE_TIER_LIMITS = {
    "requests_per_day": 1500,
    "requests_per_minute": 15,
    "tokens_per_minute": 32000
}

# Dicas para economizar cota
QUOTA_SAVING_TIPS = """
1. Use gemini-1.5-flash em vez de gemini-1.5-pro sempre que possível
2. Reduza o número de sub-agentes ativos simultaneamente
3. Implemente cache local para respostas repetitivas
4. Use dados simulados em desenvolvimento
5. Considere upgrade para plano pago para produção
"""

def get_model_for_agent(agent_type: str) -> str:
    """Retorna o modelo recomendado para um tipo de agente específico."""
    return CURRENT_MODEL_CONFIG.get(agent_type, QUOTA_EFFICIENT_MODELS["light"])

def print_quota_info():
    """Imprime informações sobre gestão de cota."""
    print("=== INFORMAÇÕES DE COTA GEMINI API ===")
    print(f"Configuração atual: Todos os agentes usando {QUOTA_EFFICIENT_MODELS['light']}")
    print(f"Limites do plano gratuito:")
    for limit, value in GEMINI_FREE_TIER_LIMITS.items():
        print(f"  - {limit}: {value}")
    print("\nDicas para economizar cota:")
    print(QUOTA_SAVING_TIPS)
