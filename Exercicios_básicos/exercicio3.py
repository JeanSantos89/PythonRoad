ano_nascimento = int(input("Qual seu ano de nascimento? "))
ano_atual = int(input("Qual o ano atual? "))

idade = ano_atual - ano_nascimento
print(f"Sua idade em ANOS é: {idade}")
print(f"Sua idade em MESES é: {idade*12}")
print(f"Sua idade em DIAS é: {idade*365}")
print(f"Sua idade em SEMANAS é: {idade*4}")

