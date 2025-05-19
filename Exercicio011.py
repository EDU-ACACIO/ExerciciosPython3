largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
tamanho = largura * altura
tinta = largura * altura / 2
print(f'Sua parede tem a dimensão de {largura}X{altura} e sua área é de {tamanho:.2f}m2')
print(f'Para pintar essa parede, você irá precisa de {tinta:.2f} litros de tinta')