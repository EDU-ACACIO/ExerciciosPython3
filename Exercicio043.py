peso = float(input('Qual é o seu peso? (Kg)'))
altura = float(input('Qual é a sua altura? (m)'))
imc = peso / (altura ** 2)
print (f'O IMC dessa pessoa é {imc:.2f}')
if imc < 18.5:
    print ('Você está ABAIXO do peso!')
elif imc >= 18.5 and imc < 25:
    print ('Você está no peso IDEAL!')
elif imc >= 25 and imc < 30:
    print ('Você está com SOBREPESO!')
elif imc >= 30 and imc < 40:
    print ('Você está com OBESIDADE!')
else:
    print ('Você está com OBESIDADE MÓRBIDA')