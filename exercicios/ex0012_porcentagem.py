# faça um programa que leia um salario e calcule um aumento de
# 15%
salario = float(input("Qual o seu salario atual ?"))
aumento = (salario * 0.15) + salario
print("Voce receberá um aumento de 15%, passando a receber R${:.2f}".format(aumento))

