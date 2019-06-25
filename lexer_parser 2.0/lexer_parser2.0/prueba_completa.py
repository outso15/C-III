import lexer_rules
import parser_rules

from ply.lex import lex
from ply.yacc import yacc

class Prueba_Completa:
    def abrir_archivo(self):
        
        expresiones = open("expresion.txt")
        linea = [" "]
        impresion = ''
        while linea != '':
           
            linea = expresiones.readline().split(' ')
            if (linea == ['']):
                expresiones.close()
                break
           
            lexer = lex(module=lexer_rules)
            parser = yacc(module=parser_rules)
            expression = parser.parse(' '.join(map(str, linea[:-1])).strip('[]'), lexer)
            
            impresion += str(expression)+'\n'
        return impresion

    def escribir_archivo(self,resultado):
        busquedas = open("resultado.txt", "w")
        busquedas.write(resultado)
        busquedas.close()

prueba = Prueba_Completa()
salida = prueba.abrir_archivo()
prueba.escribir_archivo(salida)
