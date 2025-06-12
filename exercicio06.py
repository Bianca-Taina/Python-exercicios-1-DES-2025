# Bianca está programando o controle de acesso a uma plataforma que só funciona entre 9h e 21h.
# O programa deve receber a hora atual (formato 24h) e informar se o acesso é permitido.
controle_acesso = int(input("digite o horario que voce esta tentando acessar a plataforma "))

if controle_acesso == 9:
    print("horario autorizado")
elif controle_acesso == 21:
    print("horario autorizado")
else:
    print("horario não autorizado")        
