'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.'''

from math import sqrt
oposto = float(input("Digite o valor do cateto oposto: "))
adjascente = float(input("Agora digite o valor do cateto adjascente: "))

hipotenusa = sqrt(oposto ** 2 + adjascente ** 2)
print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))


