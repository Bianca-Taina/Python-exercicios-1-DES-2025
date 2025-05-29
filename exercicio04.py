# Isabela está desenvolvendo um aplicativo de corrida que calcula a velocidade média do usuário.
# O programa deve receber a distância percorrida e o tempo gasto, calcular a velocidade e indicar se foi 
# lenta (<5 km/h), moderada (5 a 10 km/h) ou rápida (>10 km/h).
distancia = int(input("digite o valor percorrido em km/h"))
tempo = int(input("digite o tempo gasto"))

if distancia < 5 :
    print("a velocidade foi lenta")
elif distancia <= 10 :
    print(" velocidade foi moderada")
else:
    print("a velocidade foi rapida")        
