palindromo = str(input('Digite uma frase: '))
frase = palindromo.replace(' ', '')
print(f'O inverso de {palindromo} é {palindromo[::-1]}')
if frase == frase[::-1]:
    print('Temos um palindromo')
else:
    print('Não é um palindromo')