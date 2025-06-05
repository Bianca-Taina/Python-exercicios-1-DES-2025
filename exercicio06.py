# Bianca está programando o controle de acesso a uma plataforma que só funciona entre 9h e 21h.
# O programa deve receber a hora atual (formato 24h) e informar se o acesso é permitido.
controle_acesso = int(input("digite a quantidade de acesso na plataforma "))

if controle_acesso <= 9 <= 21 :
    print("a plataforma esta fechada")
elif controle_acesso <= 21 : 
    print("plataforma pode ser acessada") 
