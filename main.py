from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# Inicializar o aplicativo
app = Dash(__name__)

# Carregar os dados do Excel
df = pd.read_excel("Vendas.xlsx")

# Criar gráficos
# 1. Quantidade de Vendas por Produto
fig_produto = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group", title="Quantidade de Vendas por Produto")

# 2. Quantidade de Vendas por Loja
fig_loja = px.bar(df, x="ID Loja", y="Quantidade", title="Quantidade de Vendas por Loja")

# 3. Vendas por Mês
df['Mes'] = pd.to_datetime(df['Data']).dt.month  
vendas_por_mes = df.groupby('Mes')['Quantidade'].sum().reset_index()
fig_mes = px.line(vendas_por_mes, x='Mes', y='Quantidade', markers=True, title='Vendas por Mês')

# 4. Proporção de Vendas por Produto
fig_pizza = px.pie(df, values='Quantidade', names='Produto', title='Proporção de Vendas por Produto')

# Layout do aplicativo
app.layout = html.Div(style={'height': '100vh', 'display': 'flex', 'margin': '0'}, children=[
    # Menu lateral
    html.Div(style={'width': '20%', 'background-color': 'SteelBlue', 'padding': '10px', 'color': 'white', 'position': 'fixed', 'top': 0, 'left': 0, 'bottom': 0, 'overflowY': 'hidden', 'box-sizing': 'border-box'}, children=[
        html.Div(style={'textAlign': 'center'}, children=[
            
            html.Img(src='/assets/png2.png', style={'width': '50%', 'border-radius': '50%'}),
            html.H3("DASHBOARD DE VENDAS", style={'margin-top': '4px'})
        ]),
        html.Div(style={'flex': 1, 'padding-top': '20px'}, children=[
            html.Div(style={'display': 'flex', 'align-items': 'center', 'padding': '20px'}, children=[
                html.Img(src='/assets/home.png', style={'width': '20px', 'margin-right': '10px'}),
                dcc.Link('HOME', href='#', style={'color': 'white', 'text-decoration': 'none'})
            ]),
            html.Div(style={'display': 'flex', 'align-items': 'center', 'padding': '20px'}, children=[
                html.Img(src='/assets/carta.png', style={'width': '20px', 'margin-right': '10px'}),
                dcc.Link('MESSAGES', href='#', style={'color': 'white', 'text-decoration': 'none'})
            ]),
            html.Div(style={'display': 'flex', 'align-items': 'center', 'padding': '20px'}, children=[
                html.Img(src='/assets/coracao.png', style={'width': '20px', 'margin-right': '10px'}),
                dcc.Link('FAVORITES', href='#', style={'color': 'white', 'text-decoration': 'none'})
            ]),
            html.Div(style={'display': 'flex', 'align-items': 'center', 'padding': '20px'}, children=[
                html.Img(src='/assets/esta.png', style={'width': '20px', 'margin-right': '10px'}),
                dcc.Link('ESTATISTICS', href='#', style={'color': 'white', 'text-decoration': 'none'})
            ]),
            html.Div(style={'display': 'flex', 'align-items': 'center', 'padding': '20px'}, children=[
                html.Img(src='/assets/confi.png', style={'width': '20px', 'margin-right': '10px'}),
                dcc.Link('SETTINGS', href='#', style={'color': 'white', 'text-decoration': 'none'})
            ]),
        ])
    ]),
    # Conteúdo principal
    html.Div(style={'width': '80%', 'padding': '10px', 'display': 'flex', 'flex-direction': 'column', 'margin-left': '20%', 'box-sizing': 'border-box'}, children=[
        html.Div(style={'display': 'flex', 'justify-content': 'space-between', 'align-items': 'center', 'margin-bottom': '20px'}, children=[
            html.H1("Dashboard de Vendas", style={'textAlign': 'center', 'margin': '0', 'visibility': 'hidden'}),  
            html.Div(style={'display': 'flex', 'align-items': 'center'}, children=[
                dcc.Input(type='text', placeholder='Pesquisar...', style={'padding': '10px', 'font-size': '16px'}),
                html.Img(src='/assets/ampli.png', style={'width': '45px', 'margin-left': '0px', 'cursor': 'pointer'})
            ])
        ]),
        html.Div([
            html.Div([
                dcc.Graph(id='grafico_quantidade_vendas_produto', figure=fig_produto, style={'border': 'none', 'height': '45vh'})
            ], style={'width': '50%', 'display': 'inline-block', 'padding': '10px'}),
            html.Div([
                dcc.Graph(id='grafico_quantidade_vendas_loja', figure=fig_loja, style={'border': 'none', 'height': '45vh'})
            ], style={'width': '50%', 'display': 'inline-block', 'padding': '10px'}),
        ], style={'display': 'flex', 'flex-direction': 'row'}),
        html.Div([
            html.Div([
                dcc.Graph(id='grafico_vendas_mes', figure=fig_mes, style={'border': 'none', 'height': '45vh'})
            ], style={'width': '50%', 'display': 'inline-block', 'padding': '10px'}),
            html.Div([
                dcc.Graph(id='grafico_proporcao_vendas_produto', figure=fig_pizza, style={'border': 'none', 'height': '45vh'})
            ], style={'width': '50%', 'display': 'inline-block', 'padding': '10px'}),
        ], style={'display': 'flex', 'flex-direction': 'row'})
    ])
])

# Rodar o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)
