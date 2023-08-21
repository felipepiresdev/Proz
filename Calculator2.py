# -*- coding: utf-8 -*-
"""Calculator2

Original file is located at
    https://colab.research.google.com/drive/1eqs1LuWMzSTiD49rAxFO4u5Zyy5tuN6_
"""

def calculadora():
    while True:
        print("Operações:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        operacao = int(input("Digite o número para a operação correspondente: "))

        if operacao == 0:
            print("Saindo da calculadora.")
            break
        elif operacao < 1 or operacao > 4:
            print("Essa opção não existe.")
            continue

        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        if operacao == 1:
            resultado = numero1 + numero2
            print("Resultado:", resultado)
        elif operacao == 2:
            resultado = numero1 - numero2
            print("Resultado:", resultado)
        elif operacao == 3:
            resultado = numero1 * numero2
            print("Resultado:", resultado)
        elif operacao == 4:
            if numero2 != 0:
                resultado = numero1 / numero2
                print("Resultado:", resultado)
            else:
                print("Erro: Divisão por zero")
        else:
            print("Operação inválida")

        print("")  # Linha em branco para separar as saídas

# Iniciar a calculadora
calculadora()
