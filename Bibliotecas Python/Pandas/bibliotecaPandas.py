# Introdução a biblioteca Pandas para analise de dados
import pandas as pd # type: ignore

data = {
    'Nome': ['joao', 'maria', 'pedro'],
    'Idade': ['28', '22', '35'],
    'Cidade': ['Sao Paulo', 'Rio de Janeiro', 'Curitiba']
}

df = pd.DataFrame(data)

nomes = df['Nome']
print(nomes)

primeiraLinha = df.iloc[0]

print(primeiraLinha)