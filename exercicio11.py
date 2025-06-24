#Crie um programa que receba o peso (kg) e a altura (m) de uma pessoa e calcule o IMC.
#Classifique o resultado de acordo com a faixa:

#Abaixo do peso (< 18.5)
#Peso normal (18.5 a 24.9)
#Sobrepeso (25 a 29.9)
#Obesidade (>= 30)
altura = float(input("digite sua altura em metros."))
peso = float(input("digite seu peso em kg."))

imc = (peso / (altura * altura))

print(imc)

if imc < 18.5:
    print("abaixo do peso.")
elif imc >= 18.5 <= 24.9:
    print("peso normal.")
elif imc >= 25 <= 29.9:
    print("sobre peso.")
else:
    print("obesidade.")            