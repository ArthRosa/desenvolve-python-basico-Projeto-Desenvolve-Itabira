# -*- coding: utf-8 -*-
"""aula3.5_questao3

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_KVQxZ5Im-hP1zM04LaK1GAWoLwW4JPZ
"""

# entrada
pontuacao = int(input("Digite a pontuação do jogador: "))

# precessar
if pontuacao < 70:
    classificacao = "Insatisfatório"
elif pontuacao < 80:
    classificacao = "Regular"
elif pontuacao < 90:
    classificacao = "Bom"
else:
    classificacao = "Excelente"

# saida
print(f"Para a pontuação {pontuacao}, a classificação é: {classificacao}")