import datetime
maior = 0
menor = 0
for pessoa in range(1,8):
    ano = int(input(f'Em que ano a {pessoa}º pessoa nasceu? '))
    nascimento = datetime.date.today().year - ano
    if nascimento <= 21:
        menor = (menor + 1)
    else:
        maior= (maior + 1)
print(f'Ao todo tivemos {maior} pessoas maiores de idade')
print(f'E também tivemos {menor} pessoas menores de idade')