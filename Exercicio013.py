salario = float(input('\033[1;32mQual é o salário do funcionário ?'))
aumento = salario/100*15
final = salario + aumento
print (f'Um funcionário que ganhava R${salario}, com auemnto de 15%, passa a receber R${final:.2f}')