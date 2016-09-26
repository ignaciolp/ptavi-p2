#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

calcplus = calcoohija.Calculadorahija()

lectura = sys.argv[1]


if __name__ == "__main__":
    try:
        fichero = open(lectura, 'r')
    except:
        sys.exit("Error: Non numerical parameters")

    lineas = fichero.readlines()

    for linea in lineas:
        signo = linea.split(',')[0]
        numeros2 = linea.split(',')[2:]
        elem = int(linea.split(',')[1])
        if signo == 'resta':
            resta = elem
        if signo == 'suma':
            suma = elem
        if signo == 'multiplica':
            multiplica = elem
        if signo == 'divide':
            divide = elem
        for numero in numeros2:
            if signo == 'suma':
                suma = calcplus.sumas(suma, int(numero))
            if signo == 'resta':
                resta = calcplus.restas(resta, int(numero))
            if signo == 'divide':
                divide = calcplus.dividir(divide, int(numero))
            if signo == 'multiplica':
                multiplica = calcplus.multiplicar(multiplica, int(numero))

    print("resta = " + str(resta))
    print("suma = " + str(suma))
    print("division = " + str(divide))
    print("multiplicacion = " + str(multiplica))
