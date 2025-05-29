#  Juliana está coordenando entregas de projetos e precisa calcular o tempo total necessário 
# para finalizar três tarefas: X, Y e Z.
#  Se alguma tarefa estiver com o tempo de entrega negativo, deve-se exibir uma mensagem de 
# erro e não somar o total.
tempo03 = int(input("digite o tempo necessário para a atividade X"))
tempo02 = int(input("digite o tempo necessário para a atividade Y"))
tempo01 = int(input("digite o tempo necessário para a atividade Z"))

soma = tempo03 + tempo02 + tempo01
if tempo03 < 0:
    print("está dentro do prazo")
elif tempo02 < 0:
    print("está dentro do prazo")
elif  tempo01 < 0:      
    print("está dentro do prazo")
else:
    print("o tempo total foi " , soma)    