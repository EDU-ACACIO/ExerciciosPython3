soma = 0
for c in range(1, 7):
    numero = int(input(f'Digite o {c}º número: '))
    if numero % 2 == 0:
        soma = soma + numero
print (f'A soma dos números pares é {soma}')