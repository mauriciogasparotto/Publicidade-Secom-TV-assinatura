# Importar bibliotecas

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import warnings
warnings.filterwarnings('ignore')

# Lendo o dataframe
dfsecom_filtro = pd.read_csv(r'secom_filtrado19_23.csv', sep=',', encoding='utf-8')

# Filtrar o dataframe para cada emissora
df_globo_news = dfsecom_filtro[dfsecom_filtro['Nome do veículo'] == 'GLOBO NEWS']
df_cnn_brasil = dfsecom_filtro[dfsecom_filtro['Nome do veículo'] == 'CNN Brasil']
df_jovem_pan = dfsecom_filtro[dfsecom_filtro['Nome do veículo'] == 'JOVEM PAN NEWS TV']

# Remover prefixo "R$" e pontos de separação de milhares na coluna "Valor negociado (R$)"
df_globo_news['Valor negociado (R$)'] = df_globo_news['Valor negociado (R$)'].str.replace('R\$ ', '').str.replace('.', '').str.replace(',', '.')
df_cnn_brasil['Valor negociado (R$)'] = df_cnn_brasil['Valor negociado (R$)'].str.replace('R\$ ', '').str.replace('.', '').str.replace(',', '.')
df_jovem_pan['Valor negociado (R$)'] = df_jovem_pan['Valor negociado (R$)'].str.replace('R\$ ', '').str.replace('.', '').str.replace(',', '.')

# Converter os valores para float
df_globo_news['Valor negociado (R$)'] = df_globo_news['Valor negociado (R$)'].astype(float)
df_cnn_brasil['Valor negociado (R$)'] = df_cnn_brasil['Valor negociado (R$)'].astype(float)
df_jovem_pan['Valor negociado (R$)'] = df_jovem_pan['Valor negociado (R$)'].astype(float)

# Organizar os dataframes
df_globo_news = df_globo_news.groupby('Ano ação')['Valor negociado (R$)'].sum()
df_cnn_brasil = df_cnn_brasil.groupby('Ano ação')['Valor negociado (R$)'].sum()
df_jovem_pan = df_jovem_pan.groupby('Ano ação')['Valor negociado (R$)'].sum()

# Criar um novo DataFrame com todos os anos de interesse
df_completo = pd.DataFrame(index=range(2019, 2024))

# Preencher os valores de cada emissora no novo DataFrame
df_completo['GLOBO NEWS'] = df_globo_news
df_completo['CNN BRASIL'] = 0
df_completo.loc[2020:, 'CNN BRASIL'] = df_cnn_brasil
df_completo['JOVEM PAN NEWS TV'] = 0
df_completo.loc[2021:2022, 'JOVEM PAN NEWS TV'] = df_jovem_pan


# Definir os dados para o gráfico de barras a partir do dataset
anos = df_completo.index
valores_globo_news = df_completo['GLOBO NEWS'].values
valores_cnn_brasil = df_completo['CNN BRASIL'].values
valores_jovem_pan = df_completo['JOVEM PAN NEWS TV'].values

# Definir as cores para cada emissora
cores = ['#CD0000', '#000080', '#4F4F4F']

# Definir largura e altura do gráfico
largura = 900
altura = 630

# Criar figura e adicionar os dados das barras agrupadas
fig = go.Figure()

fig.add_trace(go.Bar(
    x=anos,
    y=valores_globo_news,
    name='GLOBO NEWS',
    marker_color=cores[0],
    hovertemplate='(%{x}, R$ %{y:,.2f} mi) GLOBO NEWS',
    #text=[f'R$ {valor/1000000:,.2f} mi' if valor > 0 else '' for valor in valores_globo_news],
    #textposition='outside'
))

fig.add_trace(go.Bar(
    x=anos,
    y=valores_cnn_brasil,
    name='CNN BRASIL',
    marker_color=cores[1],
    hovertemplate='(%{x}, R$ %{y:,.2f} mi) CNN BRASIL',
    #text=[f'R$ {valor/1000000:,.2f} mi' if valor > 0 else '' for valor in valores_cnn_brasil],
    #textposition='outside'
))

fig.add_trace(go.Bar(
    x=anos,
    y=valores_jovem_pan,
    name='JOVEM PAN NEWS TV',
    marker_color=cores[2],
    hovertemplate='(%{x}, R$ %{y:,.2f} mi) JOVEM PAN NEWS TV',
    #text=[f'R$ {valor/1000000:,.2f} mi' if valor > 0 else '' for valor in valores_jovem_pan],
    #textposition='outside'
))

# Atualizar layout do gráfico
fig.update_layout(
    plot_bgcolor='#EEE9E9',
    title={
        'text': 'Publicidade paga pela SECOM (TV por assinatura)',
        'x': 0.5,
        'y': 0.9,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    title_font=dict(size=22),
    xaxis=dict(
        title='Ano',
        title_font=dict(size=18)
    ),
    yaxis=dict(
        title='Valor (em mi R$)',
        title_font=dict(size=18),
        tickprefix='R$ ',
        ticksuffix=' mi',
        showgrid=True,
        range=[0, 6_000_000]
    ),
    barmode='group',
    width=largura,
    height=altura,
    legend=dict(x=0.98, y=0.98, xanchor='right', yanchor='top'),
    annotations=[
        go.layout.Annotation(
            text='Fonte: Gestão Secom/Dados Abertos',
            showarrow=False,
            font=dict(size=10),
            xref='paper',
            yref='paper',
            x=1,
            y=-0.1,
            xanchor='right',
            yanchor='bottom',
            align='right'
        )
    ]
)

# Exibir o gráfico
fig.show()


# Fonte: https://gestaosecom.mcom.gov.br/gestaosecom/seguranca/dados-abertos/veiculacoes-autorizadas





