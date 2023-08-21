# -*- coding: utf-8 -*-
"""Calculator.ipy

Original file is located at
    https://colab.research.google.com/drive/1u2EsW6JvErkepx2TScu4WFnDxQShcVZT
"""

def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 != 0:
            return num1 / num2
        else:
            print("Erro: Divisão por zero")
            return 0
    else:
        print("Operação inválida")
        return 0

# Exemplo de uso:
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = int(input("Digite o número da operação (1: Soma, 2: Subtração, 3: Multiplicação, 4: Divisão): "))

resultado = calculadora(numero1, numero2, operacao)
print("Resultado:", resultado)
