preco = float(input('Digite o valor do produto: R$'))
desconto = 5/100*preco
final = preco - desconto
print (f'O produto que custava {preco} na promoção com desconto de 5% irá custa R$ {final:.2f}')
