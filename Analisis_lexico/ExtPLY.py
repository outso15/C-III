import ply.lex as lex
import re
tokens = [ 'NAME','NUMBER','PLUS','MINUS','MULT','DIVIDE', 'EQUALS','OTRO' ]

t_ignore = ' \t'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_OTRO = r'[^a-z,0-9,+,*,-,/,^,=]'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex() # Build the lexer

def abrir():
    archivo = open("./expresion.txt", 'r')
    mostrar = open("./expresion.txt", 'r')
    print("La expresion es: ")
    
    for linea in archivo.readlines():               
        simb = re.split("\s", linea)
    print mostrar.readlines()    
    return simb

def lexer():    
    for lista in abrir():
        lex.input(lista)
        tok = lex.token()
        if not tok: break
        print (str(tok.value) + " - " + str(tok.type))
        
lexer()
