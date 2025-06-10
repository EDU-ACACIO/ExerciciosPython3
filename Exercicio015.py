import math

dias = float(input('\033[0;30;47mQuantos dias alugados?'))
km = float(input('Quantos Km rodados?'))
dias1 = dias * 60
km1 = km * 0.15
print (f'O total a pagar é de R${km1+dias1:.2f}')
