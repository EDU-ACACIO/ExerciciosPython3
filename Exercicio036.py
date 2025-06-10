Valorcasa = float(input('\033[1;32mQual o valor da casa? R$'))
salario = float(input('Qual o salário do comprador? R$ '))
anos = int(input('Quantos anos de financiamento? '))

financiamento = anos*12
prestacao = Valorcasa/financiamento

print(f'\033[37mPara pagar uma casa de {Valorcasa:.2f} em {anos} anos a prestação será de R$ {prestacao:.2f}.')
if prestacao < (salario * 0.30):
    print( '\033[34mEmprestimo APROVADO')
else:
    print( '\033[31mEmprestimo NEGADO')