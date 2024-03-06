'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.'''
carteira = float(input("Digite o valor a ser convertido: R$"))
valorDolar = 4.96
resultado = carteira / valorDolar

print("O valor convertido para dólar é US${:.2f}".format(resultado))