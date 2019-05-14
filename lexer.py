import ply.lex as lex
from ANALIZADOR_LEXICO2 import *

class Lexer:
    
    tokens = [ 'NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE', 'EQUALS' ]

    t_ignore = ' \t'
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_EQUALS = r':='
    t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

    def t_NUMBER(t):
        r'\d+'
        t.value = int(t.value)
        return t

    # Error handling rule
    def t_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Build the lexer
    lex.lex() 

    # Objeto de inicio
    inicio = Inicio()
    elementos = inicio.abrir_archivo()
    impresion =""
    linea = [" "]
    
    while linea != '':
        #Leer linea a linea del .txt
        linea = ' '.join(elementos.readline().split(' '))
        
        lex.input(linea)
        while True:
            tok = lex.token()
            if not tok: break
            impresion += str((str(tok.value) + " - " + str(tok.type))) + '\n'
        if (linea == ['']):
            expresiones.close()
            break
    print(impresion)
    inicio.escribir_archivo(impresion)
    
lexer = Lexer()
