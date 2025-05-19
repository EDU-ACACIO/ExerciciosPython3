import random
from time import sleep

print ('\033[1;37m-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=')
print ('Vou pensar em um número entre 0 e 5. Tente adivinhar... ')
print ('-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=')
lista = [0,1,2,3,4,5]
numero = int(input('Em que número eu pensei? '))
print ('PROCESSANDO...')
sleep(2)
escolhido = random.choice(lista)
if numero == escolhido:
    print('PARABÉNS VOCÊ CONSEGUIU ME VENCER')
else:
    print(f'ERROU! Eu pensei no número {escolhido}')