produto = float(input("digite o valor do produto: "))
percentualdescont = 5
valor_descont = (produto * percentualdescont) / 100

preco_final_com_desconto = produto - valor_descont 

print(f"O valor do desconto é 5%, seu produto sairia a {preco_final_com_desconto}, preço final sem o desconto {produto}")
