print ('='*15, 'LOJA', '='*15)
preco = float(input('Preço das compras: R$'))
print ('FORMAS DE PAGAMENTO')
print ('[ 1 ] à vista no dinheiro')
print ('[ 2 ] à vista no cartao')
print ('[ 3 ] 2x no cartao')
print ('[ 4 ] 3x ou mais no cartao')
opcao = int(input('Qual é a opção?'))
desconto_dinheiro = (10/100*preco)
final_dinheiro = preco - desconto_dinheiro
desconto_cartao = (5/100*preco)
final_cartao = preco - desconto_cartao
cartao2x = preco/2
if opcao == 1:
    print (f'Sua compra de R${preco:.2f} vai custar R${final_dinheiro:.2f} no final')
elif (opcao == 2):
    print (f'Sua compra de R${preco:.2f} vai custar R${final_cartao} no final')
elif (opcao == 3):
    print (f'Sua compra de R${preco:.2f} vai custar 2 vezes de R${cartao2x:.2f}')
elif (opcao == 4):
    vezes = int(input('Quantas parcelas?'))
    juros = (20/100*preco)
    juros1 = juros/vezes
    parcela = preco/vezes
    valor1 = (juros1+parcela)
    print (f'Sua compra será parcelada em {vezes}x de {valor1} COM JUROS')
    final2 = (20/100)*preco
    final3 = preco + final2
    print (f'Sua compra de R${preco} vai custar R${final3} no final')