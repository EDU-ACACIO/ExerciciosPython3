velocidade = float(input('Qual a velocidade atual do seu carro? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('\033[1;31mMULTADO! Você excedeu o limite permitido que é de 80km/h')
    print(f'\033[1;33mVocê irá pagar uma multa de R${multa:.2f}')
else:
    print('\033[1;36mTenha um bom dia! Dirija com segurança!')