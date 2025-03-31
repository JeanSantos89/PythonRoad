# Criar um algoritmo em PORTUGOL que informe a quantidade total de calorias de uma refeição a partir do usuário que deverá informar o prato, a sobremesa e a bebida 
# Vegetariano 180 cal - Abacaxi 75 cal          - Chá 20 cal
# Peixe 230 cal       - Sorvete diet 110 cal    - Suco de laranja 70 cal
# Frango 250 cal      - Mouse diet 170 cal      - Suco de melão 100 cal
# Carne 350 cal       - Mouse chocolate 200 cal - Refrigerante diet 65 cal



print("Indique quais as refeições que você comeu/tomou")
prato = int(input("Prato: 1. Vegetariano - 2. Peixe - 3. Frango - 4. Carne"))
sobremesa = int(input("Sobremesa: 1. Abacaxi - 2. Sorvete Diet - 3. Mousse Diet - 4. Mousse chocolate"))
bebida = int(input("Bebida: 1. Chá - 2. Suco de laranja - 3. Suco de melão - 4. Refrigerante Diet"))

if prato == 1:
    cal = 180
elif prato == 2:
    cal = 230
elif prato == 3:
    cal = 250
elif prato == 4:
    cal = 350
else:
    print("Número incorreto. Recomece.")

if sobremesa == 1:
    cal += 75
elif sobremesa == 2:
    cal += 110
elif sobremesa == 3:
    cal += 170
elif sobremesa == 4:
    cal += 200
else:
    print("Número incorreto. Recomece.")

if bebida == 1:
    cal += 20
elif bebida == 2:
    cal += 70
elif bebida == 3:
    cal += 100
elif bebida == 4:
    cal += 65
else:
    print("Número incorreto. Recomece.")


print(f"Você ingeriu {cal} calorias.")