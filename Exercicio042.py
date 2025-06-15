print ('\033[1;37mAnalisador de Triângulos')
a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento: '))

if a + b > c and a + c > b and b + c > a:
    if a == b and c == a:
        print ('Os seguimentos acima podem formar um triângulo \033[35mEQUILÁTERO')
    elif a == b or a == c or b == c:
        print ('Os seguimentos acima podem formar um triângulo \033[34mISÓCELES')
    elif a != b and b != c:
        print ('Os seguimentos acima podem formar um triângulo \033[33mESCALENO')
else:
    print ('Os seguimentos NÃO PODEM formar um triângulo')