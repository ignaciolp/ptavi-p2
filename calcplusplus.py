#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija
import csv

calcplusplus = calcoohija.Calculadorahija()

lectura =sys.argv[1] 

if __name__=="__main__":
	try:
		fichero = open(lectura,'r')
	except:
		sys.exit("Error: Non numerical parameters")

	with open(lectura) as mifichero:
		datos = csv.reader(mifichero)
		for linea in datos:
			signo = linea[0]
			numeros2 = linea[2:]
			elem=int(linea[1])
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
					suma = calcplusplus.sumas(suma, int(numero))
				if signo == 'resta':
					resta =calcplusplus.restas(resta, int(numero))
				if signo == 'divide':
					divide = calcplusplus.dividir(divide, int(numero))
				if signo == 'multiplica':
					multiplica = calcplusplus.multiplicar(multiplica, int(numero)) 
			
		
		print("resta = " + str(resta))	
		print("suma = " + str(suma))	
		print("division = " +str(divide))
		print("multiplicacion = "+ str(multiplica))	
