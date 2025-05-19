from math import sin, cos, tan, radians

angulo = float(input('\033[4;36mDigite o angulo que você deseja: '))
radianos = radians(angulo)

seno = sin(radianos)
cosseno = cos(radianos)
tangente = tan(radianos)

print (f'O ângulo de {angulo} tem o SENO de {seno:.2f}')
print (f'O ângulo de {angulo} tem o COSSENO de {cosseno:.2f}')
print (f'O ângulo de {angulo} tem a TANGENTE de {tangente:.2f}')