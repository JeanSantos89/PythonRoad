salario_colaborador = float(input("Digite o salário do colaborador: "))
incremento_salario = float(input("Digite o valor em porcentagem de incremento que deseja calcular: "))
print(f"Com o salário antigo de {salario_colaborador} e o incremento desejado de {incremento_salario}, o novo salário será de: R$ {salario_colaborador + (salario_colaborador * (incremento_salario / 100))}")