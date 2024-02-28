km = float(input("digite a quantidade de kilometros pecorridos: "))
dias = int(input("digite a quantidade de dias pelo qual o carro foi alugado: ")) 

pago = (dias * 60) + (km * 0.15)

print(f"total a pagar {pago:.2f} ")