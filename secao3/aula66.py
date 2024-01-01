#Calculadora simples:

condicao = True

while condicao:
    print()
    print("Bem vindo!! Aqui se encontra um sistema que simula uma calculadora simples!")
    print()
    sair = input("Digite'sair' para encerrar o sistema ou 'ok' para iniciar: ")
    if sair == "sair":
        break
    else:
        numero_1 = input("Digite um número: ")
        numero_2 = input("Digite outro número: ")
        operador = input("Digite um operador(+,-,/,*): ")
        print()
        if numero_1.isdigit() == True and numero_2.isdigit() == True:
            numero_1 = float(numero_1)
            numero_2 = float(numero_2)

            if operador == "+":
                resultado = numero_1 + numero_2
                print(f"O resultado de {numero_1} {operador} {numero_2} = {resultado:.2f}")
            elif operador == "-":
                resultado = numero_1 - numero_2
                print(f"O resultado de {numero_1} {operador} {numero_2} = {resultado:.2f}")
            elif operador == "/":
                resultado = numero_1 / numero_2
                print(f"O resultado de {numero_1} {operador} {numero_2} = {resultado:.2f}")
            elif operador == "*":
                resultado = numero_1 * numero_2
                print(f"O resultado de {numero_1} {operador} {numero_2} = {resultado:.2f}")
            else:
                print("Digite um operador válido!!")
        else:
            print("Digite um valor númerico!!")
    