# -*- coding: utf-8 -*-
class Libro:
    def __init__(self):
        self.titulo=""
        self.autor=""
        self.genero=""
        self.paginas=""

    def asig_atrib(self,titulo,autor,genero,paginas):
        self.titulo=titulo
        self.autor=autor
        self.genero=genero
        self.paginas=paginas
class Cola:
    """ Representa una cola con operaciones de encolar, desencolar y
        verificar si está vacía. """
 
    def __init__(self):
        """ Crea una cola vacía. """
        # La cola vacía se representa con una lista vacía
        self.items=[]

    def encolar(self, x):
        """ Agrega el elemento x a la cola. """
        # Encolar es agregar al final de la cola.
        self.items.append(x)

    def desencolar(self):
        """ Devuelve el elemento inicial y lo elimina de la cola.
            Si la cola está vacía levanta una excepción. """
        try:
            return self.items.pop(0)
        except IndexError:
            raise ValueError("La cola está vacía")

    def es_vacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.items == []
    
    def tamano(self):
       return len(self.items)

#    def buscar(self, x):
#        if(self.es_vacia==True):
#            print("No se tiene registro del libro solicitado.")
#        else:
#            for i in range(0,len(self.items)):
#                if(self.items[i].genero=='Ciencia ficcion-' ):
#                    print("\nInformacion del libro encontrado:")
                    #print(self.items[i].titulo)
                    #print(self.items[i].autor)
                    #print(self.items[i].genero)
                    #print(self.items[i].paginas)
                          
                    
                    #main()
#                else:
#                    print("No se tiene registro del libro solicitado.")
#                    print(self.items[i].titulo)
                    #main()
    
    #def getitem(self, key):
    # It's probably better to catch any IndexError to at least provide
    # a class-specific exception
    #return self.items[key]

#def main():
#    print('H')
    
    
c = Cola()
N = Cola()
import re
with open("p.txt","r") as f:
    for l in f:
        k=0
        string="nuvlibro"+str(k)
        string = Libro()
        m = re.match(r".*Libro: (.*\*).*",l)
        a = re.match(r".*Autor: (.*\/).*",l)
        g = re.match(r".*Genero: (.*\-).*",l)
        p = re.match(r".*Paginas: (.*\_).*",l)
        
        if m:
            titulo=m.group(1)
            autor=a.group(1)
            genero=g.group(1)
            paginas=p.group(1)
            string.asig_atrib(titulo,autor,genero,paginas)
           
            c.encolar(string)
            k+1

print('Ordenando libros por genero')

if(c.es_vacia==True):
    print("")
else:
    for i in range(0,len(c.items)):
        if(c.items[i].genero=='Ciencia ficcion-' ):
            N.encolar(c.items[i])
        else:
            print('.')            
if(c.es_vacia==True):
    print("")
else:
    for i in range(0,len(c.items)):
        if(c.items[i].genero=='Fantasia-' ):
            N.encolar(c.items[i])
        else:
            print('.')
if(c.es_vacia==True):
    print("")
else:
    for i in range(0,len(c.items)):
        if(c.items[i].genero=='Terror-' ):
            N.encolar(c.items[i])
        else:
            print('.')                  
F=Cola()
for i in range(0,len(N.items)):
    for j in range(1,len(N.items)):
        #print(i)
        #print(j)
        if(N.items[j].paginas<N.items[i].paginas ):
            F.encolar(N.items[j])
            #print(F.tamano())
            #print(F.items[i].titulo)
            #F.desencolar
            
            
                    #c.desencolar()            
                    #print("\nInformacion del libro encontrado:")
                    #print(c.items[i].titulo)
                    #print(N.items[i].titulo)

        if(i==j):
            #print(i)            
            F.encolar(N.items[i])
            #print(F.items[i].titulo)
        else:
            F.encolar(N.items[j])
            #print(F.tamano())
            #print('')
        

print('Liros Ordenados!')
print('Consulte el archivo: LibrosOrdenados.txt')            
import os
file = open("LibrosOrdenados.txt", "w")
file.write(N.items[0].titulo + os. linesep)
file.write(N.items[0].autor + os. linesep)
file.write(N.items[0].genero + os. linesep)
file.write(N.items[0].paginas + os. linesep)
file.write(os. linesep)
file.write(N.items[1].titulo + os. linesep)
file.write(N.items[1].autor + os. linesep)
file.write(N.items[1].genero + os. linesep)
file.write(N.items[1].paginas + os. linesep)
file.write(os. linesep)
file.write(N.items[2].titulo + os. linesep)
file.write(N.items[2].autor + os. linesep)
file.write(N.items[2].genero + os. linesep)
file.write(N.items[2].paginas + os. linesep)
file.write(os. linesep)
file.write(N.items[3].titulo + os. linesep)
file.write(N.items[3].autor + os. linesep)
file.write(N.items[3].genero + os. linesep)
file.write(N.items[3].paginas + os. linesep)
file.write(os. linesep)
file.write(N.items[4].titulo + os. linesep)
file.write(N.items[4].autor + os. linesep)
file.write(N.items[4].genero + os. linesep)
file.write(N.items[4].paginas + os. linesep)
file.write(os. linesep)
file.write(N.items[5].titulo + os. linesep)
file.write(N.items[5].autor + os. linesep)
file.write(N.items[5].genero + os. linesep)
file.write(N.items[5].paginas + os. linesep)
file.write(os. linesep)
file.write(N.items[6].titulo + os. linesep)
file.write(N.items[6].autor + os. linesep)
file.write(N.items[6].genero + os. linesep)
file.write(N.items[6].paginas + os. linesep)
file.write(os. linesep)
file.write(N.items[7].titulo + os. linesep)
file.write(N.items[7].autor + os. linesep)
file.write(N.items[7].genero + os. linesep)
file.write(N.items[7].paginas + os. linesep)
file.write(os. linesep)
file.write(N.items[8].titulo + os. linesep)
file.write(N.items[8].autor + os. linesep)
file.write(N.items[8].genero + os. linesep)
file.write(N.items[8].paginas + os. linesep)
file.write(os. linesep)
file.write(N.items[9].titulo + os. linesep)
file.write(N.items[9].autor + os. linesep)
file.write(N.items[9].genero + os. linesep)
file.write(N.items[9].paginas + os. linesep)


file.close()






