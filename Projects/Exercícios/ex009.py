'''Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.'''
n = int(input('Digite o número que deseja consultar a tabuada: \n'))
i = 1
print('Tabuada do {}: \n'.format(n))
while i <= 10:
    r = n*i
    print("{} X {} = {}".format(n,i,r))
    i = i + 1
