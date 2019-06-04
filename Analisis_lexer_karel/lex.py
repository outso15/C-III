import ply.lex as lex
import re

declaracionesiniciales = ['iniciar','terminar','definir_nueva_instruccion']

expresiones = ['expresion','fin_instruccion','inicio_instruccion','variable','numero','fin_linea']

sentencias = ['sentencia','condicion']

booleanos=['condicion_zumbador','orientacion','comprobar_libre','comprobar_bloqueo']

tokens = []+ declaracionesiniciales + expresiones + sentencias + booleanos
t_ignore = ' \t'

#Declaraciones iniciales
t_iniciar = r'(iniciar-programa|inicia-ejecucion)'
t_terminar = r'(termina-ejecucion|finalizar-programa)'
t_definir_nueva_instruccion = r'(define-nueva-instruccion|como)'

#Expresiones
t_expresion = r'(dejar-zumbador|apagate|gira-izquierda|gira-derecha|avanza|coge-zumbador|sal-de-instruccion)'
t_fin_instruccion ='fin;'
t_fin_linea=r';'
t_inicio_instruccion='inicio'
t_variable=r'([A-Z])'
t_numero=r'(\d)'

#Sentencias y condiciones
t_sentencia= r'(si|entonces|sino|mientras|hacer|repetir|veces)'
t_condicion= r'(y|o|si-es-cero|precede|sucede|no)'

#Booleanos
t_condicion_zumbador = r'(no-junto-a-zumbador|junto-a-zumbador|algun-zumbador-en-la-mochila|ningun-zumbador-en-la-mochila)'
t_orientacion =r'(orientado-al-norte|orientado-al-sur|orientado-al-este|orientado-al-oeste|no-orientado-al-norte|no-orientado-al-sur|no-orientado-al-este|no-orientado-al-oeste)'
t_comprobar_libre= r'(frente-libre|izquierda-libre|derecha-libre)'
t_comprobar_bloqueo=r'(frente-bloqueado|izquierda-bloqueada|derecha-bloqueada)'


print ("¿Cual es la ruta del archivo?:")
m = raw_input()

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex() # Build the lexer

def tokens(programa):
    lex.input(programa)
    while True:
        tok = lex.token()
        if not tok: break
        lista.append(str(tok.value) + " -> " + str(tok.type))
    return lista

archivo = open(m, "r") 
salida = open('analisis.txt',"a")
for linea in archivo.readlines():
    lex.input(linea)
    print("\nlinea : " + linea +"\n")
    salida.write("\nlinea : "+linea )   
    while True:
        tok = lex.token()
        if not tok: break
        print (str(tok.value) + " -> " + str(tok.type))
        salida.write(str(tok.value) + " -> " + str(tok.type) + " || ")
