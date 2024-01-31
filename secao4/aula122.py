import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
d2 = d1.copy()

d2['c1'] = 1000
d2['l1'][1] = 999999 # Vai mudar nos dois dicionários, porque o tipo list é mutável

print(d1)
print(d2)

d3 = copy.deepcopy(d2)

d3['l1'][0] = 55555555 # Vai mudar somente no d3, porque estou fazendo uma cópia profunda com deepcopy()

print(d1)
print(d2)
print(d3)