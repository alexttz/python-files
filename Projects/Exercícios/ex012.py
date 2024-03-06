'''Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto'''
valorOriginal = float(input("Informe o valor original do produto: R$"))
valorFinal = valorOriginal - (valorOriginal * 5 / 100)
print("O valor do produto com 5% de desconto é R${:.2f}. ".format(valorFinal))


