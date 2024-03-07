nome = input("digite seu nome completo: ")



print("O seu nome maiusculo é: " + nome.upper())
print("O seu nome minusculo é: " + nome.lower())
print("o seu nome sem contar os espaços tem : " + str(len(nome.replace(" ", ""))) + " letras")
primeiro_nome = nome.split(" ")[0]
print(f"o seu primeiro nome tem {len(primeiro_nome)} letras")

