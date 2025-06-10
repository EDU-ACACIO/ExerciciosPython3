print ('\033[36m=-'*20)
print ('\033[31mAnalisador de Triângulos')
print ('\033[36m=-'*20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and a + c > b and b + c > a:
    print('Os segmentos acima PODEM FORMAR um Triângulo')
else:
    print('Os seguimentos acima NÃO PODEM formar um Triângulo')