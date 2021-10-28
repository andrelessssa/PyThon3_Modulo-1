# modulos , podemos importar
# math - matematica - ceil (arredondat pra cima)
#  floor( arredondar pra baixo)

from math import sqrt, floor
num = int(input("Digite um número: "))
raiz = sqrt(num)
print("A raiz de {} é igual a {:.2f}".format(num,floor(raiz)))

# import random
# num = random.randint(1,10)
# print(num)