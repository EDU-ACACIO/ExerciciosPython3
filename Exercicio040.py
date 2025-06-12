n1 = float(input('\033[1;37mDigite sua primeira nota: '))
n2 = float(input('\033[1;37mDigite sua segunda nota: '))
media = (n1 + n2) / 2

print (f'Tirando \033[0m{n1}\033[1;37m e \033[0m{n2}\033[0m \033[1;37ma média do aluno é \033[0m{media}\033[0m')
if media >= 7:
    print ('\033[1;37mO aluno está \033[1;34m APROVADO')
elif media < 7 and media >= 6:
    print ('\033[1;37mO aluno está de \033[1;33m RECUPERAÇÃO')
else:
    print ('\033[1;37mO aluno está \033[1;31mREPROVADO')