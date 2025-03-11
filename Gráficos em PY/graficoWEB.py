import plotly.express as px  # Importa a biblioteca Plotly Express para visualização de dados
import plotly.graph_objects as go  # Importa a biblioteca Graph Objects do Plotly

# Carrega o conjunto de dados "iris" que contém informações sobre flores da espécie Iris
df = px.data.iris()

# Cria um gráfico de dispersão mostrando a relação entre 'sepal_width' e 'sepal_length'
# As cores representam diferentes espécies de flores
temp_fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species', title='Iris Sepal Dimensions')

# Conta o número de amostras para cada espécie
species_count = df['species'].value_counts()

# Cria um gráfico de barras para visualizar a contagem de amostras por espécie
fig = go.Figure(data=[go.Bar(
    x=species_count.index,  # Define o eixo X com os nomes das espécies
    y=species_count.values,  # Define o eixo Y com a contagem de cada espécie
    text=species_count.values,  # Exibe os valores das barras no gráfico
    textposition='auto'  # Posiciona automaticamente os rótulos de texto
)])

# Atualiza o layout do gráfico de barras, definindo título e rótulos dos eixos
fig.update_layout(
    title='Número de Amostras por Espécie',  # Define o título do gráfico
    xaxis_title='Espécie',  # Rótulo do eixo X
    yaxis_title='Contagem'  # Rótulo do eixo Y
)

# Exibe o gráfico
fig.show()