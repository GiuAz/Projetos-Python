from pathlib import Path

# Define o caminho do arquivo
caminhoDoArquivo = Path("nomesAmigos.txt")

# Dados para salvar no arquivo
dadosParaSalvar = ["Rafael", "Marcus", "Cruz", "Lucas"]

# Abre o arquivo no modo 'W' (escrita) e salva os dados
with caminhoDoArquivo.open(mode='w') as arquivo:
    for item in dadosParaSalvar:
        arquivo.write(f"{item}\n")

print("Dados salvos com sucesso!")

# Abre o arquivo no modo 'R' (Leitura) e lê os dados
with caminhoDoArquivo.open(mode='r') as arquivo: 
    dadosLidos = arquivo.readlines()

# Remove os caracteres de nova linha 
dadosLidos = [linha.strip() for linha in dadosLidos]

print("Dados lidos do arquivo:", dadosLidos)
