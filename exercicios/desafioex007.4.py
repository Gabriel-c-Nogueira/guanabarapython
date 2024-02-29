import random 

aluno1 = input("digite um nome: ")
aluno2 = input("digite um nome: ")
aluno3 = input("digite um nome: ")
aluno4 = input("digite um nome: ")

lista_alunos = [aluno1, aluno2, aluno3, aluno4]

nome_sorteado = random.sample(lista_alunos, 1)

print(f"o aluno sorteado foi {nome_sorteado}")