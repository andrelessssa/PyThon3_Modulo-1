# Escreva um programa que pergunte a quantidade de km
# percorrido por um carro e dias que foi alugado ,calcule o
# preço a pagar , sabendo que o carro custa 80 por dia
# e 0,15 por km rodado.

dia = int(input("Quantos dias ficou alugado? "))
km = float(input("Quantos Km rodados? "))
pago = (dia * 60) + (km * 0.15)
print("O total a pagar é de R${:.2f}".format(pago))



