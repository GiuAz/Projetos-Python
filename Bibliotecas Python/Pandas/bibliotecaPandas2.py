# Introdução à biblioteca Pandas para análise de dados
import pandas as pd  # type: ignore

# Criar um DataFrame a partir de um dicionário
data = {
    'Nome': ['Giu', 'Nat', 'Rafa'],
    'Idade': [23, 20, 24],  # Idade como números
    'Bairro': ['Imirim', 'Jaragua', 'Cachoeirinha']
}

df = pd.DataFrame(data)
print("DataFrame criado: \n", df)

# Salvar o DataFrame em um arquivo CSV
df.to_csv('clientes.csv', index=False, encoding='utf-8')
print("\nArquivo 'clientes.csv' criado com sucesso!")

# Ler dados de um arquivo CSV
dfCSV = pd.read_csv('clientes.csv')
print("\nDataFrame lido do CSV: \n", dfCSV)

# Selecionar a coluna 'Bairro'
bairros = df['Bairro']
print("\nBairros: \n", bairros)

# Filtrar clientes com idade maior que 21
filtroIdade = dfCSV[dfCSV['Idade'] > 21]
print("\nClientes com idade maior que 21: \n", filtroIdade)
