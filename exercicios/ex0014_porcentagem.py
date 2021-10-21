# qual o valor do produto
produto = float(input("Digite o valor do produto: R$"))
desconto = (produto * 5 / 100)
print("Voce tera um desconto de 5% e pagará R${:.2f}".format((produto - desconto)))

