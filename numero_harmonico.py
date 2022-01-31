n = 100
soma_ed = 0
soma_de  = 0

for i in range (1, n+1):
    soma_ed += 1/i
    soma_de += 1/(n+1-i)

print("Soma ED  :", soma_ed)
print("Soma DE  :", soma_de)
print("Diferenca:", soma_de-soma_ed)
