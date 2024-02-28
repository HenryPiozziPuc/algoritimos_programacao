salario = float(input("Insira seu salario "))
reajuste = float(input("Insira seu reajuste "))

salario_ajustado = salario*(1+reajuste/100)

print(f"\n\n Seu salario de {salario:.2f} após o reajuste de {reajuste:.2f}% se tornou {salario_ajustado:.2f}")