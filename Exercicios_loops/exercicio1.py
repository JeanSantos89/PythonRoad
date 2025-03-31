"""Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
 No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. 
 O seu resultado fica sendo a média dos três valores restantes. 
 Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a 
 média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). 
 Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. 
 O programa deve ser encerrado quando não for informado o nome do atleta.
"""

def calcular_media(saltos):
    melhor_salto = max(saltos)
    pior_salto = min(saltos)
    saltos.remove(melhor_salto)
    saltos.remove(pior_salto)
    media_salto = sum(saltos) / len(saltos)
    return melhor_salto, pior_salto, media_salto

nome = input("Qual o nome da/do atleta? ")
while nome == '':
    nome = input("Qual o nome da atleta? ")

saltos = []
for x in range (1,6):
    salto = float(input(f"Digite a distância do salto: "))
    saltos.append(salto)


print(f"Atleta: {nome}")
print(f"Primeiro salto: {saltos[0]}m")
print(f"Segundo salto: {saltos[1]}m")
print(f"Terceiro salto: {saltos[2]}m")
print(f"Quarto salto: {saltos[3]}m")
print(f"Quinto salto: {saltos[4]}m")
melhor_salto, pior_salto, media_salto= calcular_media(saltos)
print(f"O menor salto foi de {pior_salto}m")
print(f"O maor salto foi de {melhor_salto}m")
print(f"A média dos saltos foi de: {media_salto}m")

