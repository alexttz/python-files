'''Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.'''

c = float(input("Digite o valor em graus celsius: "))
f = c * 1.8 + 32

print("Os graus em Farenheit é: {:.0f}. ".format(f))