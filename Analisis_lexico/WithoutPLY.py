import re
def lex():
    str = " 1 2 + 4 3 / * 2 = a"
    y = re.split("\s", str)
    print("Esta es la expresion en postfijo: " )
    print str
    print ("Ahora veremos de que tipo es cada uno de sus terminos")
    for lista in y:
        Valor(lista)
        Variables(lista)
        Operadores(lista)
        Otros(lista)

def Valor(lista):
    valor = "[0-9]"
    v = re.findall(valor, lista)
    if (v):
        print ("%s " %v + " Valor ")
    return v

def Variables(lista):
    variable = "[a-z]"
    var = re.findall(variable, lista)
    if (var):
        print ("%s " %var + " Variable")
    return var

def Operadores(lista):
    operador = "[-,*,+,/,^,=]"
    op = re.findall(operador, lista)
    if (op):
        print ("%s " %op + " Operador")
    return op

def Otros(lista):
    otro="[^a-z,0-9,+,*,-,/,^,=]"
    otro = re.findall(otro,lista)
    if(otro):
        print("%s " %otro + " Otro")
    return otro

lex()
