# Multi-Tool Urban Management Agent

Sistema multi-agente para gestão urbana utilizando Google Gemini API.

## ⚠️ Gestão de Cota da API

### Problema de Cota Excedida

Se você recebeu o erro `429 RESOURCE_EXHAUSTED`, significa que excedeu os limites do plano gratuito da API Gemini.

### Soluções Implementadas

1. **Modelos Otimizados**: Todos os agentes agora usam `gemini-1.5-flash` que consome menos cota
2. **Configuração Flexível**: Sistema de configuração em `quota_config.py` para fácil ajuste
3. **Redução de Complexidade**: Simplificação das instruções para reduzir tokens

### Limites do Plano Gratuito

- **Requisições por dia**: 1.500
- **Requisições por minuto**: 15  
- **Tokens por minuto**: 32.000

### Como Economizar Cota

1. **Aguarde o Reset**: A cota reseta a cada 24 horas
2. **Use Flash Model**: `gemini-1.5-flash` consome ~10x menos cota que `gemini-1.5-pro`
3. **Reduza Testes**: Teste com dados mockados quando possível
4. **Upgrade do Plano**: Considere upgrade para plano pago para uso intensivo

### Estrutura do Projeto

```
multi_tool_agent/
├── agent.py          # Agentes principais
├── quota_config.py   # Configurações de cota
├── __init__.py       # Exportação do root_agent
└── .env             # Chaves da API
```

### Agentes Disponíveis

1. **Detection Agent**: Detecção de problemas urbanos
2. **Risk Agent**: Avaliação de riscos
3. **Registration Agent**: Cadastro de problemas
4. **Analysis Agent**: Análise de dados
5. **Management Agent**: Gestão de pendências
6. **Supervisor Agent**: Coordenação geral (root_agent)

### Como Usar

```python
from multi_tool_agent import root_agent

# O root_agent coordena todos os sub-agentes automaticamente
response = root_agent.process("Detectar problemas na Broadway")
```

### Monitoramento de Cota

Execute o arquivo `quota_config.py` para ver dicas de economia:

```bash
python quota_config.py
```

### Próximos Passos

1. Aguarde 24h para reset da cota
2. Considere implementar cache local
3. Para produção, upgrade para plano pago
4. Implemente rate limiting no seu código
