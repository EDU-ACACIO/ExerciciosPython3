numero = int(input('\033[1;37mDigite um número inteiro: '))
print ('Escolha uma das bases para conversão: ')
print ('\033[1;31m[1] Converter para BINÁRIO')
print ('\033[1;34m[2] Converter para OCTAL')
print ('\033[1;33m[3] Converter para HEXADECIMAL')
opcao = int(input())

print (f'\033[1;37msua opção: {opcao}')
if opcao == 1:
    print(f'\033[1;31m{numero} convertido para BINÁRIO é igual a {bin(numero)[2:]}')
elif opcao == 2:
    print(f'\033[1;34m{numero} convertido para OCTAL é igual a {oct(numero)[2:]}')
elif opcao == 3:
    print(f'\033[1;33m{numero} convertido para HEXADECIMAL é igual a {hex(numero)[2:]}')
else:
    print('OPÇÃO INVÁLIDA TENTE NOVAMENTE')