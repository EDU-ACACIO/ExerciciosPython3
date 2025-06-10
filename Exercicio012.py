preco = float(input('\033[1;36mQual é o preço do produto?'))
desconto = 5/100*preco
final = preco - desconto
print(f'O produto que custava R${preco}, na promoção com desconto de 5% vai custar R${final:.2f}')
