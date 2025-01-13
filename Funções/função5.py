def verificarIdade(idade):
    if idade >= 18:
        return "maior de idade"
    else:
        return "menor de idade"

idadeUsuario = int(input("Digite sua idade: "))
status = verificarIdade(idadeUsuario) 

print(f"Voce e {status}.")