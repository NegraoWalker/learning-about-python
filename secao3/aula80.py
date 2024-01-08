minha_lista = [1, 2, 3, "quatro", 5.0]


print(minha_lista[0])
print(minha_lista[3])
print(minha_lista[-2])

minha_lista[0] = "Walker"
print(minha_lista)

minha_lista.append("Negrão")
print(minha_lista)

del minha_lista[4]
print(minha_lista)

minha_lista.insert(1,133)
print(minha_lista)

minha_lista.pop(0)
print(minha_lista)

minha_lista2 = ["Laranja", 1.778, 3, True]

# minha_lista3 = minha_lista + minha_lista2
minha_lista.extend(minha_lista2)

print(minha_lista)