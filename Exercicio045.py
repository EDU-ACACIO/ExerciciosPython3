import random
from time import sleep

print ('\033[1;37mSuas opções: ')
print ('[0] PEDRA')
print ('[1] PAPEL')
print ('[2] TESOURA')
lista = ['PEDRA', 'PAPEL', 'TESOURA']
jogada = int(input('Qual é a sua jogada?'))

print ('-='*13)
print ('\033[1;33mJO')
sleep(1)
print ('\033[1;34mKEN')
sleep(1)
print ('\033[1;35mPÔ')
print('-='*13)

escolhido = random.randint(0,2)

print (f'\033[31mComputador jogou {lista[escolhido]}')
print (f'\033[34mJogador jogou {lista[jogada]}')

if jogada == 0 and escolhido == 1:
    print ('\033[31mCOMPUTADOR GANHOU')
elif jogada == 1 and escolhido == 2:
    print ('\033[31mCOMPUTADOR GANHOU')
elif jogada == 2 and escolhido == 0:
    print ('\033[31mCOMPUTADOR GANHOU')
elif jogada == escolhido:
    print ('\033[33mEMPATE')
else:
    print ('\033[34mJOGADOR GANHOU')