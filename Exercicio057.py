sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor informe seu sexo: ')).strip().upper()[0]
if sexo == 'M' or sexo == 'F':
    print(f'Sexo {sexo} registrado com sucesso.')