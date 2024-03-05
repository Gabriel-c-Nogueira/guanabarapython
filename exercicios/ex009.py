frase = ["curso em video python"]

frase.len(frase) #calcula o tamanho da frase 
frase.count("ex")
frase.count("o", 0, 13) # ele vai contar quantos (o) tem na frase e até o indice 13 mas não exatamente ao 13 e sim ao 12
frase.find("deo") # ele encontra onde começou o deo, no caso indice 13 então frase.find("deo") = 13
"curso" in frase 
frase.replace('python', 'android')
frase.upper()
frase.lower()
frase.captalize()
frase.title()
frase.strip() #ele remove os caracteres vazios do começo e do fim da string
frase.rstrip() # remove apenas os ultimos espaços começando pela direita
frase.lstrip() # remove apenas os primeiros espaços começando pela esquerda
frase.split() # ele divide o elemento em varias partes, onde tiver espaço ele divide basta usar " "
"-".join(frase) # ele junta os caracteres separados e usando o -/ curso-em-video

