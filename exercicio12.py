#Peça ao usuário uma senha e verifique se ela contém pelo menos 8 caracteres.
#Exiba uma mensagem de "Senha válida" ou "Senha muito curta".
usuario  = input("Digite sua senha ")

if len(usuario) >= 8:
    print("senha valida")
else:
    print("senha muito curta")
