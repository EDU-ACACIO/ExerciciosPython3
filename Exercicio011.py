largura = float(input('\033[34mlargura da parede: '))
altura = float(input('altura da parede: '))
tamanho = largura*altura
tinta = largura*altura/2
print (f'Sua parede tem a dimensão de {largura}X{altura} e sua área é de {tamanho:.2f}m2')
print (f'Para pintar essa parede, você precisará de {tinta:.2f}l de tinta.')