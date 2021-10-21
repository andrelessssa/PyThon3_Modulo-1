# faça um programa que leia a largura e altura de uma parede
# e calcule a area e a quantidade de tinta para pintar
# a cada litro pinta 2m quadrados
largura = float(input("Digite o valor da largura: "))
altura = float(input("Digite o valor da Altura: "))
area = largura * altura
tinta = area / 2
print("Area da parede vale {}, voce precisa de {} litros de Tinta.".format(area, tinta))
