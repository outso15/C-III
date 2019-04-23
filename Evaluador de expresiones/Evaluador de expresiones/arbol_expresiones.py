from pila import *
from arbol import *
from cola import *
def convertir(lista, pila):
    if lista != []:
        if lista[0] in "+-*/":
            nodo_der = pila.desapilar()
            nodo_izq = pila.desapilar()
            pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
        else:
            pila.apilar(Nodo(lista[0]))
        return convertir(lista[1:],pila)
            
def evaluar(arbol):
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    return int(arbol.valor)


pila = Pila()
N= Cola()
print('Rectifique que el archivo expresiones.in ')
print('tenga 3 operaciones en postfijo separadas por espacio y por renglon')
print(' ')
print('Realizando la evaluacion de expresiones...')

archivo = open("expresiones.in.txt", "r")
lista = archivo.readlines()
k=0
for contenido in lista:
    expr='exp'+str(k)
    contenido = contenido.strip("\n")
    expr= (contenido.split(" "))
    k=k+1
    print('.')
    #print(contenido , k
    #print(contenido.split(" "))9
    convertir(expr, pila)
    N.encolar('Expresión '+str(k) + ' = ' +str(evaluar(pila.desapilar())))
import os
import re
print('Evaluacion correcta! revise el archvo expresiones.out al cerrar la ventana')

file = open("expresiones.out.txt", "w")
file.write(N.items[0] + os. linesep)
file.write(N.items[1] + os. linesep)
file.write(N.items[2] + os. linesep)


