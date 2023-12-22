primeiro_numero = input("Digite um número: ")
segundo_numero = input("Digite outro número: ")

primeiro_numero = float(primeiro_numero)
segundo_numero = float(segundo_numero)

if primeiro_numero > segundo_numero:
    print(f"{primeiro_numero=:.2f} é maior o {segundo_numero=:.2f}")
elif segundo_numero > primeiro_numero:
    print(f"{segundo_numero=:.2f} é maior o {primeiro_numero=:.2f}")
else:
    print(f"Os número são iguais: {primeiro_numero=:.2f} == {segundo_numero=:.2f}")
