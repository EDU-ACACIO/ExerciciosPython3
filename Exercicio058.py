import random
soma = 1
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue advinhar qual foi?')

numero = int(input('Qual é seu palpite? '))
lista = [0,1,2,3,4,5,6,7,8,9,10]
escolhido = random.choice(lista)

while numero != escolhido:
    soma = soma + 1
    if numero > escolhido:
        print('Menos... Tente novamente')
        numero = int(input())
        if numero == escolhido:
            print('Parabéns você conseguiu me vencer!')
    elif numero < escolhido:
        print('Mais... Tente novamente')
        numero = int(input())
        if numero == escolhido:
            print('Parabéns você conseguiu me vencer!')
print(f'Você acertou com {soma} tentativas.')