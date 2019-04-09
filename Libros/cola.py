# -*- coding: utf-8 -*-
class Libro:
    def __init__(self):
        self.titulo=""
        self.autor=""
        self.genero=""
        self.paginas=""
        self.editorial=""

    def asig_atrib(self,titulo,autor,genero,paginas,editorial):
        self.titulo=titulo
        self.autor=autor
        self.genero=genero
        self.paginas=paginas
        self.editorial=editorial
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
        e = re.match(r".*Editorial: (.*\+).*",l)
        
        if m:
            titulo=m.group(1)
            autor=a.group(1)
            genero=g.group(1)
            paginas=p.group(1)            
            editorial=e.group(1)            
            string.asig_atrib(titulo,autor,genero,paginas,editorial)           
            c.encolar(string)
            k+1

print('Ordenando libros por genero y editorial')

if(c.es_vacia==True):
    print("")
else:
    for i in range(0,len(c.items)):
        if(c.items[i].genero=='Ciencia ficcion-' and c.items[i].editorial=='Gnome Press+' ):
            N.encolar(c.items[i])        
        else:
            print('.')

if(c.es_vacia==True):
    print("")
else:
    for i in range(0,len(c.items)):        
        if(c.items[i].genero=='Ciencia ficcion-' and c.items[i].editorial=='Scholastic+' ):
            N.encolar(c.items[i])
        else:
            print('.')

            
if(c.es_vacia==True):
    print("")
else:
    for i in range(0,len(c.items)):
        if(c.items[i].genero=='Fantasia-' and c.items[i].editorial=='Bantam Spectra+' ):
            N.encolar(c.items[i])        
        else:
            print('.')

            
if(c.es_vacia==True):
    print("")
else:
    for i in range(0,len(c.items)):
        if(c.items[i].genero=='Fantasia-' and c.items[i].editorial=='Bloomsbury Publishing+' ):
            N.encolar(c.items[i])
        else:
            print('.')
            
if(c.es_vacia==True):
    print("")
else:
    for i in range(0,len(c.items)):
        if(c.items[i].genero=='Fantasia-' and c.items[i].editorial=='George Allen & Unwin+' ):
            N.encolar(c.items[i])
        else:
            print('.')
            
if(c.es_vacia==True):
    print("")
else:
    for i in range(0,len(c.items)):
        if(c.items[i].genero=='Fantasia-' and c.items[i].editorial=='Scholastic+' ):
            N.encolar(c.items[i])
        else:
            print('.')

            
if(c.es_vacia==True):
    print("")
else:
    for i in range(0,len(c.items)):
        if(c.items[i].genero=='Terror-' and c.items[i].editorial=='Gold Medal Books+' ):
            N.encolar(c.items[i])
        else:
            print('.')

if(c.es_vacia==True):
    print("")
else:
    for i in range(0,len(c.items)):
        if(c.items[i].genero=='Terror-' and c.items[i].editorial=='Norma+' ):
            N.encolar(c.items[i])
        else:
            print('.')

if(c.es_vacia==True):
    print("")
else:
    for i in range(0,len(c.items)):
        if(c.items[i].genero=='Terror-' and c.items[i].editorial=='Viking Press+' ):
            N.encolar(c.items[i])
        else:
            print('.')         
print('Liros Ordenados!')
print('Consulte el archivo: LibrosOrdenados.txt')            
import os
file = open("LibrosOrdenados.txt", "w")
file.write('___________________________________________')
file.write(os. linesep)
file.write('Libro: '+ N.items[0].titulo + os. linesep)
file.write('Autor: '+ N.items[0].autor + os. linesep)
file.write('Genero: ' + N.items[0].genero + os. linesep)
file.write('Paginas: '+ N.items[0].paginas + os. linesep)
file.write('Editorial: '+ N.items[0].editorial + os. linesep)
file.write('___________________________________________')
file.write(os. linesep)
file.write('___________________________________________')
file.write(os. linesep)
file.write('Libro: '+ N.items[1].titulo + os. linesep)
file.write('Autor: '+ N.items[1].autor + os. linesep)
file.write('Genero: ' + N.items[1].genero + os. linesep)
file.write('Paginas: '+ N.items[1].paginas + os. linesep)
file.write('Editorial: '+ N.items[1].editorial + os. linesep)
file.write('___________________________________________')
file.write(os. linesep)
file.write('___________________________________________')
file.write(os. linesep)
file.write('Libro: '+ N.items[2].titulo + os. linesep)
file.write('Autor: '+ N.items[2].autor + os. linesep)
file.write('Genero: ' + N.items[2].genero + os. linesep)
file.write('Paginas: '+ N.items[2].paginas + os. linesep)
file.write('Editorial: '+ N.items[2].editorial + os. linesep)
file.write('___________________________________________')
file.write(os. linesep)
file.write('___________________________________________')
file.write(os. linesep)
file.write('Libro: '+ N.items[3].titulo + os. linesep)
file.write('Autor: '+ N.items[3].autor + os. linesep)
file.write('Genero: ' + N.items[3].genero + os. linesep)
file.write('Paginas: '+ N.items[3].paginas + os. linesep)
file.write('Editorial: '+ N.items[3].editorial + os. linesep)
file.write('___________________________________________')
file.write(os. linesep)
file.write('___________________________________________')
file.write(os. linesep)
file.write('Libro: '+ N.items[4].titulo + os. linesep)
file.write('Autor: '+ N.items[4].autor + os. linesep)
file.write('Genero: ' + N.items[4].genero + os. linesep)
file.write('Paginas: '+ N.items[4].paginas + os. linesep)
file.write('Editorial: '+ N.items[4].editorial + os. linesep)
file.write('___________________________________________')
file.write(os. linesep)
file.write('___________________________________________')
file.write(os. linesep)
file.write('Libro: '+ N.items[5].titulo + os. linesep)
file.write('Autor: '+ N.items[5].autor + os. linesep)
file.write('Genero: ' + N.items[5].genero + os. linesep)
file.write('Paginas: '+ N.items[5].paginas + os. linesep)
file.write('Editorial: '+ N.items[5].editorial + os. linesep)
file.write('___________________________________________')
file.write(os. linesep)
file.write('___________________________________________')
file.write(os. linesep)
file.write('Libro: '+ N.items[6].titulo + os. linesep)
file.write('Autor: '+ N.items[6].autor + os. linesep)
file.write('Genero: ' + N.items[6].genero + os. linesep)
file.write('Paginas: '+ N.items[6].paginas + os. linesep)
file.write('Editorial: '+ N.items[6].editorial + os. linesep)
file.write('___________________________________________')
file.write(os. linesep)
file.write('___________________________________________')
file.write(os. linesep)
file.write('Libro: '+ N.items[7].titulo + os. linesep)
file.write('Autor: '+ N.items[7].autor + os. linesep)
file.write('Genero: ' + N.items[7].genero + os. linesep)
file.write('Paginas: '+ N.items[7].paginas + os. linesep)
file.write('Editorial: '+ N.items[7].editorial + os. linesep)
file.write('___________________________________________')
file.write(os. linesep)
file.write('___________________________________________')
file.write(os. linesep)
file.write('Libro: '+ N.items[8].titulo + os. linesep)
file.write('Autor: '+ N.items[8].autor + os. linesep)
file.write('Genero: ' + N.items[8].genero + os. linesep)
file.write('Paginas: '+ N.items[8].paginas + os. linesep)
file.write('Editorial: '+ N.items[8].editorial + os. linesep)
file.write('___________________________________________')
file.write(os. linesep)
file.write('___________________________________________')
file.write(os. linesep)
file.write('Libro: '+ N.items[9].titulo + os. linesep)
file.write('Autor: '+ N.items[9].autor + os. linesep)
file.write('Genero: ' + N.items[9].genero + os. linesep)
file.write('Paginas: '+ N.items[9].paginas + os. linesep)
file.write('Editorial: '+ N.items[9].editorial + os. linesep)

file.close()






