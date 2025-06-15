numero = int(input('Digite um número: '))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        total = total + 1
        print('\033[34m', end='')
    else:
        print('\033[31m', end='')
    print(c,'\033[0m', end='')
print('ACABOU')
if total == 2:
    print(f'O número {numero} foi divisível {total} vezes.')
    print('Por isso ele é primo')
else:
    print(f'O número {numero} foi divisivel {total} vezes.')
    print('Por isso ele NÃO é primo')