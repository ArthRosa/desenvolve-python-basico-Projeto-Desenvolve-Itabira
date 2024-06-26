# -*- coding: utf-8 -*-
"""aula2_questao 1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_KVQxZ5Im-hP1zM04LaK1GAWoLwW4JPZ
"""

def data_por_extenso(data):
    # Lista com os nomes dos meses
    meses = [
        'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
        'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
    ]

    # Separar o dia, mês e ano da data
    dia, mes, ano = data.split('/')

    # Converter o mês para inteiro
    mes = int(mes)

    # Imprimir a data formatada com o nome do mês por extenso
    print(f"Você nasceu em {dia} de {meses[mes - 1]} de {ano}.")

# Solicitar data de nascimento ao usuário
data_nascimento = input("Digite uma data de nascimento (dd/mm/aaaa): ")

# Chamar a função para imprimir a data por extenso
data_por_extenso(data_nascimento)