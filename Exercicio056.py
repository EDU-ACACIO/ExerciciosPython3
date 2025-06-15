idadetotal = 0
velho = 0
mulher = 0
maisvelho = 0
for pessoa in range(1,5):
    print(f'----- {pessoa}º pessoa -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    idadetotal = idadetotal + idade
    sexo = str(input('Sexo: [M/F]: ')).upper()
    if sexo == 'M':
        if idade > velho:
            velho = idade
            maisvelho = nome
    if sexo == 'F' and idade < 20:
        mulher = mulher + 1
print(f'A média de idade do grupo é de {idadetotal/4} anos.')
print(f'O homem mais velho tem {velho} anos e se chama {maisvelho} anos.')
print(f'Ao todo são {mulher} mulheres com menos de 20 anos.')