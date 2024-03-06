"""Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele."""
n = input("Digite algo: ")
print('O tipo primitivo da variável é',type(n))

print('O tipo de dado possue somente espaços? ', n.isspace())
print('O tipo de dado é uma letra? ', n.isalpha())
print('O tipo de dado é um número? ', n.isnumeric())
print('O tipo de dado é alfanumérico? ', n.isalnum())
print('O tipo de dado está em maiúsculo? ', n.isupper())
print('O tipo de dado está em minúsculo? ', n.islower())
print('O tipo de dado está em capitalizada? ', n.istitle())
