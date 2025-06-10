nome  = str(input('\033[37;40mDigite seu nome completo: ')).strip()
print (f'\033[37;40mMuito prazer em te conhecer!\033[0m')
print (f'\033[37;40mSeu primeiro nome é {nome.split()[0]}\033[0m')
print (f'\033[37;40mSeu ultimo nome é {nome.split()[-1]}\033[0m')