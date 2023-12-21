nome = input("Qual o seu nome? ")
print(type(nome), nome)
print(f"Seu nome é {nome=}")


# numero_1 = float(input("Informe um número: "))
# numero_2 = float(input("Informe um número: "))
# print(f"A soma dos dois números é {numero_1 + numero_2:.2f}")

numero_1 = input("Informe um número: ")
numero_2 = input("Informe um número: ")

float_numero_1 = float(numero_1)
float_numero_2 = float(numero_2)

print(f"A soma dos dois números é {float_numero_1 + float_numero_2:.2f}")