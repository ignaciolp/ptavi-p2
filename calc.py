#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


def plus(op1, op2):
    """ Function to sum the operands """
    return op1 + op2


def minus(op1, op2):
    """ Function to substract the operands """
    return op1 - op2


def multi(op1, op2):
    """funcion de multiplicacion"""
    return op1 * op2


def divi(op1, op2):
    """funcion de dividir"""
    if operando1 == 0 or operando2 == 0:
        return " No se puede dividir con ceros"
    else:
        return op1 / op2


if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = plus(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = minus(operando1, operando2)
    elif sys.argv[2] == "multiplicar":
        result = multi(operando1, operando2)
    elif sys.argv[2] == "dividir":
        result = divi(operando1, operando2)

    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

    print(result)
