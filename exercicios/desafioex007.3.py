import math

angulo = float(input("digite o angulo em graus: "))

angulo_rad = math.radians(angulo)


seno = math.sin(angulo_rad)
coss = math.cos(angulo_rad)
tang = math.tan(angulo_rad)

print(f"O valor do seno é {seno}, o valor do cosseno é {coss} e o valor da tangente é {tang}")