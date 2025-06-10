'''primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
terceiro = int(input('Terceiro valor: '))
if primeiro > segundo and primeiro > terceiro:
    maior = primeiro
    print(f'O maior valor digitado foi {maior}')
if segundo > primeiro and segundo > terceiro:
    maior = segundo
    print(f'O maior valor digitado foi {maior}')
if terceiro > primeiro and terceiro > segundo:
    maior = terceiro
    print(f'O menor valor digitado foi {maior}')
if primeiro < segundo and primeiro < terceiro:
    menor = primeiro
    print (f'O menor valor digitado foi {menor}')
if segundo < primeiro and segundo < terceiro:
    menor = segundo
    print(f'O menor valor digitado foi {menor}')
else:
    menor = terceiro
    print(f'O menor valor digitado foi {menor}')'''

primeiro = int(input('\033[1;33mPrimeiro valor: '))
segundo = int(input('Segundo valor: '))
terceiro = int(input('Terceiro valor: '))
lista = [primeiro, segundo, terceiro]

maior = max(lista)
menor = min(lista)
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')