'''Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.'''
altura = float(input("Informe a altura da parede em metros: "))
largura = float(input("Em seguida, informe em metros a largura a ser calculada: "))

area = largura * altura
valorTinta = area / 2

print("A área da parede é de {:.2f}m² e serão necessários {:.1f}L para pintá-la. ".format(area,valorTinta))