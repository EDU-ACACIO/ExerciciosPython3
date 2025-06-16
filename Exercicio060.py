numero = int(input('Digite um número para calcular seu fatorial: '))
resultado = 1
while numero > 0:
    resultado = resultado * numero
    print(numero, end=' ')
    print(' x ' if numero > 1 else ' = ', end='')
    numero = numero - 1
print(resultado)