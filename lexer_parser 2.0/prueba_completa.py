import lexer_rules
import parser_rules
import getFile

from ply.lex import lex
from ply.yacc import yacc

text = getFile.getFiles()
lexer = lex(module=lexer_rules)
parser = yacc(module=parser_rules)
expression = parser.parse(text, lexer)
print expression
"""
result = expression.evaluate()
print result
"""
