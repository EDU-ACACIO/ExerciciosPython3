import random
nome = str(input('Primeiro aluno: '))
nome1 = str(input('Primeiro aluno: '))
nome2 = str(input('Primeiro aluno: '))
nome3 = str(input('Primeiro aluno: '))
lista = [nome, nome1, nome2, nome3]
random.shuffle(lista)
print(f'A ordem de apresentação será: {lista}')