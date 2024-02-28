comprimento = float(input("Insira o comprimento da sala "))
largura = float(input("Insira a largura da sala "))
carpete = float(input("Insira o preço do carpete por metro quadrado "))
preco_total = comprimento*largura*carpete
print(f"\n\n\tO preço para cobrir o chão dessa sala será {preco_total:.2f} reais")