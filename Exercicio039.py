from datetime import date

sexo = input('\033[1;37mDigite seu sexo \033[0m(\033[1;34mM\033[0m/\033[31mF\033[0m): ').strip().upper()

if sexo == 'F':
    print('\033[1;37mO alistamento militar não é obrigatório para mulheres')
    exit()

elif sexo not in ('M','F'):
    print ('Digite uma opção válida')
    exit()

nascimento = int(input('\033[1;37mDigite o seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nascimento
maior = idade - 18
menor = 18 - idade

print (f'Quem nasceu em {nascimento} tem {idade} anos em {ano_atual}')
if idade == 18:
    print ('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    print (f'Ainda faltam {menor} anos para o alistamento')
    print (f'Seu alistamento será em {ano_atual + menor}.')
elif idade > 18:
    print (f'\033[1;31mVocê já deveria ter se alistado há {maior} anos.')
    print (f'Seu alistamento foi em {ano_atual - maior}.')