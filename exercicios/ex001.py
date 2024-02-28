from datetime import datetime 


nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))
ano_atual = datetime.now().year

subtracao = ano_atual -  idade  
print(f'olá, {nome}, você nasceu em {subtracao}')