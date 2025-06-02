# Diego está acompanhando seu consumo de internet mensal, que tem um limite de 100 GB.
# O programa deve receber o total consumido e avisar se ele ultrapassou o limite.
consumo_internet = int(input("digite o consumo total de internet "))

if consumo_internet < 100 :
    print(f"total consumido {consumo_internet}")
else:
    print("ultrapassou o limite ")    

