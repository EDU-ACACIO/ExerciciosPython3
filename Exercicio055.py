pesos = []

for pessoa in range(1,6):
    peso = float(input(f'Digite o peso da pessoa {pessoa}º pessoa: '))
    pesos.append(peso)

print(f'O maior peso é {max(pesos)}')
print(f'O menor peso é {min(pesos)}')