'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''

km = float(input("Informe a quantidade de KMs percorridos: "))
dias = int(input("Informe os dias que o carro foi alugado: "))

ValorPagar = (km * 0.15) + (dias * 60)

print("O valor a ser pago do aluguel é de R${:.2f}. ".format(ValorPagar))
