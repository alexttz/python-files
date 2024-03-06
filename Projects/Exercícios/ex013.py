'''Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.'''

salario = float(input("Informe o seu salário atual: R$"))
novoSalario = salario + (salario * 15 / 100)

print("Com o reajuste de 15% o novo salário é de R${:.2f}. ".format(novoSalario))
