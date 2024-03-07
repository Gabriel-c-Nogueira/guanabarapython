frase = "curso em video python"

v1 = len(frase) #calcula o tamanho da frase 
v2 = frase.count("ex")
v3 = frase.count("o", 0, 13) # ele vai contar quantos (o) tem na frase e até o indice 13 mas não exatamente ao 13 e sim ao 12
v4 = frase.find("deo") # ele encontra onde começou o deo, no caso indice 13 então frase.find("deo") = 13
v5 = "curso" in frase # retorna um valor booleano se o parametro esta ou não incluido em frase
v6 = frase.replace('python', 'android') # o proprio nome ja diz, ele troca itens, elementos da lista ou string 
v7 = frase.upper() # passa itens da str para maiusculo
v8 = frase.lower() # passa itens e elementos de str para minusculo 
v9 = frase.capitalize() # passa o primeiro caracter para maiusculo e o resto para minusculo
v10 = frase.title() # passa para maiusculo todas as primeiras letras em cada palavra
v11 = frase.strip() #ele remove os caracteres vazios do começo e do fim da string
v12 = frase.rstrip() # remove apenas os ultimos espaços começando pela direita
v13 = frase.lstrip() # remove apenas os primeiros espaços começando pela esquerda
v14 = frase.split() # ele divide o elemento em varias partes, onde tiver espaço ele divide basta usar " "
v15 = "-".join(frase) # ele junta os caracteres separados e usando o -/ curso-em-video


print(v1, " (1) // len(frase) // calcula o tamanho da frase \n")
print(v2, "(2) // frase.count(""ex"") // calcula a quantidade do item escolhido na str exemplo ""v2 = frase.count(""ex"" \n ")
print(v3, "(3) // frase.count(""o"", 0, 13) // ele vai contar quantos (o) tem na frase a partir do indice 0 até o indice 13 mas não exatamente ao 13 e sim ao 12 \n")
print(v4, "(4) // frase.find(""deo"") // ele encontra onde começou o deo, no caso indice 13 então frase.find(""deo"") = 13  caso não tenha o elemento na lista ele da -1 = não encontrado\n")
print(v5, "(5) // curso in frase // retorna um valor booleano se o parametro esta ou não incluido em frase \n")
print(v6, "(6) // frase.replace('python', 'android') // o proprio nome ja diz, ele troca itens, elementos da lista ou string \n")
print(v7, "(7) // frase.upper() // passa itens da str para maiusculo \n " ) 
print(v8, "(8) // frase.lower() // passa itens e elementos de str para minusculo \n ")
print(v9, "(9) // frase.capitalize() // passa o primeiro caracter para maiusculo e o resto para minusculo \n ")
print(v10, "(10) // frase.title() // passa para maiusculo todas as primeiras letras em cada palavra \n ")
print(v11, "(11) // frase.strip() // ele remove os caracteres vazios do começo e do fim da string \n")
print(v12, "(12) // frase.rstrip() // remove apenas os ultimos espaços começando pela direita \n")
print(v13, "(13) //  frase.lstrip() // remove apenas os primeiros espaços começando pela esquerda \n")
print(v14, "(14) //   frase.split() // ele divide o elemento em varias partes, onde tiver espaço ele divide basta usar " " \n ")
print(v15, "(15) //    ""-"".join(frase) // ele junta os caracteres separados e usando o -/ curso-em-video \n""")
