import random
nome = str(input('\033[1;31mPrimeiro aluno: '))
nome1 = str(input('Segundo aluno: '))
nome2 = str(input('Terceiro aluno: '))
nome3 = str(input('Quarto aluno: '))
lista = [nome, nome1, nome2, nome3]
random.shuffle (lista)
print (f'A ordem de apresentação será: {lista}')