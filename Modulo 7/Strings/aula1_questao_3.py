# -*- coding: utf-8 -*-
"""aula1_questao 3

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_KVQxZ5Im-hP1zM04LaK1GAWoLwW4JPZ
"""

# Solicita ao usuário que digite a frase
frase = input("Digite a frase: ")

# Inicializa o contador de espaços em branco
contagem = 0

# Itera sobre cada caractere na frase
for caractere in frase:
    if caractere == ' ':  # Verifica se o caractere é um espaço em branco
        contagem += 1  # Incrementa o contador de espaços em branco

# Imprime o total de espaços em branco encontrados
print(f"Espaços em branco: {contagem}")