n1 = int(input("digite um valor: "))
n2 = int(input("digite outro valor: "))

s = n1 + n2 
m = n1 * n2 
d = n1 / n2 
di = n1 // n2 
e = n1 ** n2 

print(f"a soma é {s}, o produto é {m} e a divisão é {d:.3f}", end=' --->>> ') #// para quebrar a linha basta usar \n
print(f"A divisão inteira é {di} e potencia é {e}")