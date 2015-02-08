#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Calculadora.
Ejecutar $ python calc.py [ sumar, restar, dividir, multiplicar] [num1 num2]

"""
import sys


def sumar(a, b):
    return a+b


def restar(a, b):
    return a-b


def mult(a, b):
    return a*b


def dividir(a, b):
    return a/b
try:
    if __name__ == "__main__":
        if len(sys.argv) != 4:
            sys.exit("Usage: $ python calc.py [ function] [num1 num2] ")
        func = sys.argv[1]
        op1 = int(sys.argv[2])
        op2 = int(sys.argv[3])
        if func == 'sumar':
            print sumar(op1, op2)
        elif func == 'multiplicar':
            print mult(op1, op2)
        elif func == 'restar':
            print restar(op1, op2)
        elif func == 'dividir':
            try:
                print 'C= ' + str(dividir(op1, op2)) + ' R= ' + str(op1 % op2)
            except ZeroDivisionError:
                print ' MATH_ ERROR :Intentas dividir entre 0'
        else:
            print
            sys.exit("Usage: calc.py [function][num1 num2]")
except ValueError:
    print ' Introduce dos numeros enteros.'
