# #1°
# def generator():
#     n=1
#     yield n
#     print("Continuando")
#     n+=1
#     yield n
#     print("Mais uma")
#     n+=1
#     yield n
#     print("Vou terminar")
#     return "Terminou!"


# gen = generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# #2°
# def generator(n=0, maximum=10):
#     while True:
#         yield n
#         n += 1

#         if n >= maximum:
#             return


# gen = generator()
# for n in gen:
#     print(n)

#3°
def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return


gen = generator(maximum=100)
for n in gen:
    print(n)