from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
print('=-'*13)
opcao = 0
while opcao != 5:
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos números')
    print('[ 5 ] Sair do programa')
    opcao = int(input('Qual é sua opção? '))
    if opcao == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}')
        print('=-'*13)
        sleep(1)
    elif opcao == 2:
        print(f'O resultado de {n1} X {n2} é igual a {n1 * n2}')
        print('=-'*13)
        sleep(1)
    elif opcao == 3:
        if n1 > n2:
            print(f'O maior número é {n1}')
            print('=-'*13)
            sleep(1)
        elif n1 < n2:
            print(f'O maior número é {n2}')
            print('=-'*13)
            sleep(1)
        else:
            print('Os dois números são iguais')
    elif opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(1)
        print('Saindo do programa...')
        exit()
    else:
        print('Digite uma opção válida')
        print('=-'*13)