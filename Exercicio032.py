from datetime import date
atual = date.today().year
ano = int(input('\033[7;31mQue ano quer analisar? Coloque 0 para analisar o ano atual:'))
if ano == 0:
    print(f'{atual}\033[0m')
elif ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto\033[0m')
else:
    print(f'O ano {ano} não é bissexto\033[0m')
