import math

x = int(input("digite o comprimento do cateto oposto: "))
y = int(input("digite o comprimento do cateto adjacente: "))

hipo = math.hypot(x, y)
print(f"A hipotenusa é {round(hipo)}")
