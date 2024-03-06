'''Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.'''

nota1 = float(input('Digite o valor da nota da P1: '))
nota2  = float(input('Agora digite o valor da nota da P2: '))

notafinal = (nota1 + nota2) / 2

print('A nota final do aluno foi {:.1f}'.format(notafinal))
