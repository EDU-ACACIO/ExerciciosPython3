distancia = float(input('\033[1;37mQual é a distância da sua viagem? '))
print(f'Você está prestes a começar sua viagem de {distancia} km!')
if distancia <= 200:
    kms = distancia * 0.50
    print(f'E o preço da sua passagem é R${kms:.2f}')
else:
    kms = distancia * 0.45
    print(f'E o preço da sua passagem é R${kms:.2f}')