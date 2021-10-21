# Adição +
# Subtração -
# Multiplicação *
# Divisão /
# Potencia **
# Divisão inteira //
# Resto da Divisão % 
# ORDEM DE PRESCEDENCIA
# 1 - ()
# 2 - **
# 3 - * / // %
# 4 - + -
a = 5 + 3 * 2
print(a)
b = 5 ** 2  # potencia
print(b)
c = pow(5, 2)  # potencia
print(c)
d = 81 ** (1 / 2)  # raiz quadrada
print(d)
nome = input("Qual o seu nome?")
print("Prazer em conhecer {}".format(nome))
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print("A soma é {}, O produto é {}, e a divisao é {} ".format(s, m, d))
print("A divisao inteira é {}, e a potencia é {}".format(di, e))
