from datetime import date

nascimento = int(input('\033[1mAno de nascimento: '))
idade = date.today().year - nascimento

print (f'O atleta tem {idade} anos')
if idade <= 9:
    print('Classificação: \033[35mMIRIM')
elif idade <= 14:
    print('Classificação: \033[34mINFANTIL')
elif idade <= 19:
    print('Classificação: \033[33mJUNIOR')
elif idade <= 25:
    print('Classificação: \033[31mSÊNIOR')
else:
    print('Classificação: \033[37mMASTER')