#Simule um login com nome de usuário "admin" e senha "1234".
#Caso os dados estejam corretos, exiba "Acesso concedido", senão "Acesso negado"
usuario = input("Digite o nome do usuario ")
senha = input("Digite sua senha ")

if usuario == "admin" and senha == "1234":
   print("Acesso concebido")
else:
   print("Acesso negado")