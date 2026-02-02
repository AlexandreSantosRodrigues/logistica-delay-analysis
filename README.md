📊 Etapas do Projeto
1. ETL e Pré-processamento (Python)
Nesta fase, utilizei Python para tratar o dataset original que continha variáveis em inglês e códigos numéricos.

Data Cleaning: Padronização de strings e tratamento de nulos.

Tradução: Conversão total de categorias para Português.

Otimização: Tipagem de dados para redução do consumo de memória no motor VertiPaq do Power BI.

2. Modelagem de Dados (Power BI - Star Schema)
Abandonei o uso de tabelas "flat" (única tabela larga) em favor de um Esquema Estrela (Star Schema).

Tabela Fato: Fato_Vendas contendo chaves estrangeiras e métricas transacionais.

Tabelas Dimensão: Dim_Produto, Dim_Cliente, Dim_Geografia e uma dCalendario robusta em DAX.

Vantagem: Maior performance de processamento e garantia de integridade nas relações 1:N.

3. Inteligência de Dados com DAX
As métricas foram construídas utilizando a técnica de Measure Branching (ramificação de medidas), garantindo código limpo e reutilizável.

Lead Time Real:
Lead Time Real = DATEDIFF(Fato_Vendas[data_pedido], Fato_Vendas[data_envio_real], DAY)

Crescimento de Vendas (YoY):
Crescimento Vendas % = DIVIDE([Total Vendas] - [Vendas LY], [Vendas LY], 0)
Pareto de Atrasos: Cálculo acumulado para identificar os 20% de produtos que geram 80% dos atrasos.

🎯 A Solução: Diagnóstico de Atrasos Multi-Label
O maior desafio deste projeto foi prever a causa dos atrasos com múltiplos rótulos. A solução foi implementada através de três frentes analíticas:

Análise de Dispersão (Clusters): Ao cruzar Lead Time Real vs. Valor do Pedido, identifiquei se o atraso era Operacional Interno (preparação lenta) ou Logístico Externo (falha na transportadora).

Pareto de Ofensores: Identificação exata de quais categorias de produtos retêm o maior volume de atrasos, permitindo ações de estoque direcionadas.

Árvore de Decomposição (IA): Utilização de Inteligência Artificial para decompor o status "Atrasado" e encontrar automaticamente as variáveis de maior influência (ex: correlação entre modo de envio e segmento de cliente).

📈 Dashboard Final
Visão de Composição de Status: Panorama de performance por canal.

Concentração de Atrasos: Foco no que realmente importa (80/20).

Correlação Operacional: Identificação de gargalos de tempo vs. ticket médio.

Explorador de Causas Raiz: Diagnóstico assistido por IA.

![LOGISTICA - DASHBOARD](https://github.com/user-attachments/assets/82e532d4-e251-4805-bce8-057c78df92a3)

