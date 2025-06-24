#Peça três números e exiba-os em ordem crescente.
numeros = []

for i in range(0, 3, 1):
    numeros.append(int(input("Digite um numero: ")))

numeros.sort()
print(numeros)    
