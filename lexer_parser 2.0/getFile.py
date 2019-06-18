# -*- coding: utf-8 -*-

def getFiles():
    print ("¿Cual es la ruta del archivo?:")
    m = raw_input()
    archivo = open(m,'r')
    filas = (archivo.read().splitlines())
    return filas

if __name__  == '__main__':
    getFiles()
