# -*- coding: utf-8 -*-
"""Birthday

Original file is located at
    https://colab.research.google.com/drive/1MXGxVKDXNzfqdeeDCyh6g2zHEal3QaVK
"""

import datetime

def obter_ano_nascimento():
    while True:
        try:
            ano = int(input("Digite o ano de nascimento (entre 1922 e 2023): "))
            if 1922 <= ano <= 2023:
                return ano
            else:
                print("Ano fora do intervalo permitido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Insira um número válido.")

def calcular_idade(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

def main():
    nome = input("Digite o seu nome completo: ")
    ano_nascimento = obter_ano_nascimento()
    idade = calcular_idade(ano_nascimento)
    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")

if __name__ == "__main__":
    main()
