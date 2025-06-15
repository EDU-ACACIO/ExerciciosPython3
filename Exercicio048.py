soma = 0
total = 0
for contador in range(1, 501, 2):
    if contador % 3 == 0 and contador % 2 != 0:
        soma = soma + contador
        total = total + 1
print (f'A soma de todos os {total} valores solicitado é de {soma}')