import pandas as pd
import os

def localizar_arquivo(nome):
    for dirname, _, filenames in os.walk('/kaggle/input'):
        for filename in filenames:
            if filename == nome:
                return os.path.join(dirname, filename)
    return nome

caminho = localizar_arquivo('incom2024_delay_example_dataset.csv')
df = pd.read_csv(caminho)

mapa_conteudo = {
    'customer_segment': {
        'Consumer': 'Consumidor', 'Corporate': 'Corporativo', 'Home Office': 'Home Office'
    },
    'order_status': {
        'COMPLETE': 'Concluído', 'PENDING': 'Pendente', 'PROCESSING': 'Processando', 
        'CLOSED': 'Fechado', 'ON_HOLD': 'Em Espera', 'PENDING_PAYMENT': 'Pagamento Pendente', 
        'PAYMENT_REVIEW': 'Revisão de Pagamento', 'CANCELED': 'Cancelado', 'SUSPECTED_FRAUD': 'Suspeita de Fraude'
    },
    'market': {
        'Africa': 'África', 'Europe': 'Europa', 'LATAM': 'América Latina', 
        'Pacific Asia': 'Ásia-Pacífico', 'USCA': 'EUA/Canadá'
    },
    'shipping_mode': {
        'Standard Class': 'Classe Padrão', 'Second Class': 'Segunda Classe', 
        'First Class': 'Primeira Classe', 'Same Day': 'Mesmo Dia'
    },
    'payment_type': {
        'DEBIT': 'Débito', 'TRANSFER': 'Transferência', 'CASH': 'Dinheiro', 'PAYMENT': 'Pagamento'
    },
    'department_name': {
        'Footwear': 'Calçados', 'Fan Shop': 'Artigos Esportivos', 'Apparel': 'Vestuário', 
        'Golf': 'Golfe', 'Outdoors': 'Atividades ao Ar Livre', 'Discs Shop': 'Loja de Discos', 
        'Fitness': 'Fitness', 'Technology': 'Tecnologia', 'Pet Shop': 'Pet Shop', 
        'Health and Beauty ': 'Saúde e Beleza', 'Book Shop': 'Livraria'
    },
    'order_region': {
        'Western Europe': 'Europa Ocidental', 'South America': 'América do Sul', 'Central America': 'América Central', 
        'East of USA': 'Leste dos EUA', 'West of USA ': 'Oeste dos EUA', 'Southeast Asia': 'Sudeste Asiático', 
        'West Africa': 'África Ocidental', 'Southern Europe': 'Europa do Sul', 'Oceania': 'Oceania', 
        'Northern Europe': 'Europa do Norte', 'West Asia': 'Ásia Ocidental', 'South Asia': 'Sul da Ásia', 
        'Caribbean': 'Caribe', 'South of  USA ': 'Sul dos EUA', 'Eastern Europe': 'Europa Oriental', 
        'US Center ': 'Centro dos EUA', 'Eastern Asia': 'Ásia Oriental', 'North Africa': 'Norte da África', 
        'Southern Africa': 'África Austral', 'Central Africa': 'África Central', 'Canada': 'Canadá', 
        'East Africa': 'África Oriental', 'Central Asia': 'Ásia Central'
    },
    'customer_country': {
        'Puerto Rico': 'Porto Rico', 'EE. UU.': 'EUA'
    }
}

for col, mapa in mapa_conteudo.items():
    if col in df.columns:
        df[col] = df[col].replace(mapa)

df['order_date'] = pd.to_datetime(df['order_date'])
df['shipping_date'] = pd.to_datetime(df['shipping_date'])

map_label = {-1: 'Chegada Antecipada', 0: 'No Prazo', 1: 'Atrasado'}
df['label'] = df['label'].map(map_label)

traducoes_colunas = {
    'payment_type': 'tipo_pagamento', 'profit_per_order': 'lucro_por_pedido',
    'sales_per_customer': 'vendas_por_cliente', 'category_id': 'id_categoria',
    'category_name': 'nome_categoria', 'customer_city': 'cidade_cliente',
    'customer_country': 'pais_cliente', 'customer_id': 'id_cliente',
    'customer_segment': 'segmento_cliente', 'customer_state': 'estado_cliente',
    'customer_zipcode': 'cep_cliente', 'department_id': 'id_departamento',
    'department_name': 'nome_departamento', 'latitude': 'latitude_loja',
    'longitude': 'longitude_loja', 'market': 'mercado_destino',
    'order_city': 'cidade_entrega', 'order_country': 'pais_entrega',
    'order_customer_id': 'id_cliente_pedido', 'order_date': 'data_pedido',
    'order_id': 'id_pedido', 'order_item_cardprod_id': 'id_item_produto_rfid',
    'order_item_discount': 'valor_desconto_item', 'order_item_discount_rate': 'taxa_desconto_item',
    'order_item_id': 'id_linha_pedido', 'order_item_product_price': 'preco_item_unitario',
    'order_item_profit_ratio': 'margem_lucro_item', 'order_item_quantity': 'quantidade_itens',
    'sales': 'venda_bruta', 'order_item_total_amount': 'valor_total_item',
    'order_profit_per_order': 'lucro_total_pedido', 'order_region': 'regiao_entrega',
    'order_state': 'estado_entrega', 'order_status': 'status_pedido',
    'product_card_id': 'id_produto', 'product_category_id': 'id_categoria_produto',
    'product_name': 'nome_produto', 'product_price': 'preco_tabela_produto',
    'shipping_date': 'data_envio_real', 'shipping_mode': 'modo_envio',
    'label': 'status_entrega'
}

df = df.rename(columns=traducoes_colunas)

for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].astype(str).str.strip()

df.to_csv('logistica_totalmente_em_portugues.csv', index=False)

print("✅ Tudo pronto! O arquivo foi traduzido por dentro e por fora.")
df.head()
