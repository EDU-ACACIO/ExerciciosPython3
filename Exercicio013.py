salario = float(input('Qual é o salário do funcionário? R$'))
aumento = salario * 0.15
final = salario + aumento
print (f'Um funcionário que ganhava R${salario:.2f}, com aumento de 15%, passa a receber R${final:.2f}')