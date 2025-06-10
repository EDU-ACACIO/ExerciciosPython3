salario = (float(input('\033[7;34mQual é o salário do funcionário? R$')))
if salario >= 1250:
    aumento = (10/100)*salario+salario
else:
    aumento = (15/100)*salario+salario
print (f'Quem ganhava R${salario:.2f} passa a ganhar R${aumento:.2f} agora\033[0m')