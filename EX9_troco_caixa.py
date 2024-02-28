import math


valor_compra = float(input("Insira o valor da compra em reias "))
valor_pago = float(input("Insira o valor pago pelo cliente "))
troco = valor_pago - valor_compra
notas20 = 0
notas10 = 0
notas5 = 0
notas1 = 0

if troco < 0:
    print("ainda há valor a pagar")
else:
    notas20 = math.floor(troco/20)
    troco = troco%20
    notas10 = math.floor(troco/10)
    troco = troco%10
    notas5 = math.floor(troco/5)
    troco = troco%5
    notas1 = troco

    print(f"\n\nTroco: {troco}\n em:\n{notas20:.0f} notas de 20\n{notas10:.0f} notas de 10\n{notas5:.0f} notas de 5\n{notas1:.0f} notas de 1")



    
