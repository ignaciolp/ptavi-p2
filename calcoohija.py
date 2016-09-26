#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo


class Calculadorahija(calcoo.Calculadora):

    def multiplicar(self, op1, op2):
        return op1*op2

    def dividir(self, op1, op2):
        if op2 == 0:
            return "Division by zero is not allowed"
        else:
            return op1/op2

if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operandor2 = str(sys.argv[2])
        operando3 = int(sys.argv[3])

    except ValueError:
        sys.exit("Error: Non numerical parameters")

    calculadorahija = Calculadorahija()

    if operandor2 == "suma":
        result = calculadorahija.sumas(operando1, operando3)
    elif operandor2 == "resta":
        result = calculadorahija.restas(operando1, operando3)
    elif operandor2 == "multiplicar":
        result = calculadorahija.multiplicar(operando1, operando3)
    elif operandor2 == "dividir":
        result = calculadorahija.dividir(operando1, operando3)
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

    print(result)
