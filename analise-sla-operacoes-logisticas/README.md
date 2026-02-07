# Análise de SLA Logístico e Simulação de Otimização de Transportadoras

## Visão Geral
Este projeto realiza uma análise de desempenho logístico com foco em SLA de entrega, utilizando dados simulados de pedidos, regiões e transportadoras.  
O objetivo principal é avaliar taxas de atraso e simular um cenário de melhoria operacional, removendo a pior transportadora em cada SLA para medir o impacto na performance.

O resultado final é apresentado em um dashboard analítico desenvolvido no Power BI, com tratamento e simulação de dados realizados em Python.

---

## Objetivos do Projeto
- Avaliar a taxa de entregas atrasadas por SLA
- Identificar a pior transportadora em cada SLA com base na taxa de atraso
- Simular a remoção dessas transportadoras
- Comparar os cenários antes e depois da simulação
- Apoiar decisões estratégicas de gestão logística baseadas em dados

---

## Estrutura dos Dados
Principais campos utilizados na análise:

- `order_id`: identificador único do pedido  
- `region`: região de entrega  
- `carrier_name`: nome da transportadora  
- `sla_days`: prazo de entrega acordado (em dias)  
- `delivered_late`: indicador de atraso (True ou False)

---

## Etapas do Processo

### 1. Preparação dos Dados
- Limpeza e validação da base
- Conversão do indicador de atraso para métricas agregáveis
- Agrupamento por SLA e transportadora

### 2. Métricas do Cenário Base
Para cada SLA, são calculadas:
- Total de pedidos
- Total de pedidos atrasados
- Taxa de atraso (%)

### 3. Identificação da Pior Transportadora
- Cálculo da taxa de atraso por transportadora dentro de cada SLA
- Identificação da transportadora com maior taxa de atraso em cada SLA

### 4. Simulação de Otimização
- Remoção da pior transportadora identificada em cada SLA
- Reprocessamento das métricas
- Novo cálculo da taxa de atraso após a simulação

### 5. Comparação de Cenários
- Comparação direta entre o cenário original e o cenário simulado
- Cálculo da melhoria em pontos percentuais na taxa de atraso

---

## Visualizações no Power BI
O dashboard final contém:

- Gráfico de colunas comparando a taxa de atraso antes e depois da simulação por SLA
- Gráfico de barras exibindo a redução da taxa de atraso em pontos percentuais
- KPIs executivos destacando o impacto médio da otimização simulada

---

## Principais Insights
- A remoção de transportadoras com baixo desempenho reduz de forma consistente a taxa de atraso
- O impacto da otimização varia de acordo com o SLA, indicando oportunidades específicas de melhoria
- A simulação demonstra como análises de dados podem apoiar decisões estratégicas na gestão logística

---

## Tecnologias Utilizadas
- Python (pandas)
- Power BI
- Git e GitHub

---

## Próximos Passos
- Simular a substituição das transportadoras removidas por novos parceiros
- Aplicar pesos por volume de pedidos para métricas globais
- Expandir a análise considerando recortes regionais