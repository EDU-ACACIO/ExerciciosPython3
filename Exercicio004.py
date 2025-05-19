msg = input('\033[7;37;40mDigite algo:')
print('O tipo primitivo desse valor é ',type(msg))
print('Só tem espaços? ',msg.isspace())
print('É numerico?', (msg.isnumeric()))
print('É alfabetico?',(msg.isalpha()))
print('É alfanumerico?',(msg.isalnum()))
print('Está em maiusculo?',(msg.isupper()))
print('Está em minusculo?',(msg.islower()))
print('Está capitalizada?',(msg.istitle()))



