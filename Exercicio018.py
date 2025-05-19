import math

angulo = float(input('Digite o angulo que você deseja: '))
radianos = math.radians(angulo)

seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

print(f'O seno de {angulo} é {seno:.2f}')
print(f'O cosseno de {angulo} é {cosseno:.2f}')
print(f'A tangente de {angulo} é {tangente:.2f}')