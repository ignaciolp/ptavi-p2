#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora():

    def sumas(self, op1, op2):
        return op1+op2

    def restas(self, op1, op2):
        return op1-op2

if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
        calculadora = Calculadora()
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = calculadora.sumas(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = calculadora.restas(operando1, operando2)
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

    print(result)
