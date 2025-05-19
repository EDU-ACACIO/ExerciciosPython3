import random
nome = str(input('\033[36mDigite o nome do aluno: '))
nome1 = str(input('Digite o nome do aluno: '))
nome2 = str(input('Digite o nome do aluno: '))
nome3 = str(input('Digite o nome do aluno: '))
lista = [nome, nome1, nome2, nome3]
escolhido = random.choice (lista)
print (f'O aluno escolhido foi: {escolhido}')