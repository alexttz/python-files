'''Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.'''

valorMetros = float(input('Digite o valor em metros: '))
valorDec = valorMetros * 10
valorCent = valorMetros * 100
valorMili = valorMetros * 1000
valorDeca = valorMetros / 10
valorHeca = valorMetros / 100
valorKm = valorMetros / 1000
print('Os valores são:\nDecímetros: {}dm\nCentímetros: {}cm\nMilímetros: {}mm\nDecâmetros: {}dam\nHecatômetros: {}hm\nKilômetros: {}km\n '.format(valorDec,valorCent,valorMili,valorDeca,valorHeca, valorKm))