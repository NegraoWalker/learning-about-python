string_a = "Valor"
string_b = string_a

print(string_a)
print(string_b)

string_a = "Valor2"

print(string_a) 
print(string_b) # String é imutável, não ocorre a alteração do valor. Porque aponta para endereços de memória diferentes

lista_a = [105,True,False,"Oi"]

lista_b = lista_a

print(lista_a)
print(lista_b)

lista_a[0] = "Troquei o Valor!"

print(lista_a)
print(lista_b) # List é mutável, ocorre a alteração do valor. Porque aponta para endereços de memória iguais