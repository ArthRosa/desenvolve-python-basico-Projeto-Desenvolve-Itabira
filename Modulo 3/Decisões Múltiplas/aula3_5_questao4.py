# -*- coding: utf-8 -*-
"""aula3.5_questao4

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_KVQxZ5Im-hP1zM04LaK1GAWoLwW4JPZ
"""

# entrada
valor_total = float(input("Digite o valor total da compra: "))


desconto_percentual = 0.0


if valor_total >= 100:
    desconto_percentual = 20.0
elif valor_total >= 50:
    desconto_percentual = 10.0
else:
    desconto_percentual = 0.0

# processando
desconto = (desconto_percentual / 100) * valor_total


valor_final = valor_total - desconto


print(f"Desconto aplicado: {desconto_percentual}%")

#saida
print(f"Valor final com desconto: R${valor_final:.2f}")