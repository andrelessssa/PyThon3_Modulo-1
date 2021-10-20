# Faça um programa que leia algo
# pelo teclado e mostre na tela
# o seu tipo primitivo e todas as informa coes
a1 = input("Digite algo no teclado: ")
print("Voce digitou: {}".format(a1))
print("O tipo é ", type(a1))
print("Só tem espaço: ", a1.isspace())
print("É um número? ",a1.isnumeric())
print("É alfanumérico?  ",a1.isalpha())




