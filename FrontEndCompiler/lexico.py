'''
Analisador lexico
Alunos: Douglas Gomes de Paula - Matricula: 11621BCC013
        Miguel Sanches Rocha - Matricula: 11811BCC001
'''

import re

f = open("prog.txt", "r")

def nextChar():
    return f.read(1)

def fail():
    print("informar o erro")

class Token:
    def __init__(self, tipo, atributo, linha, coluna):
        self.tipo = tipo
        self.atributo = atributo
        self.linha = linha
        self.coluna = coluna

class Atributo:
    def __init__(self,nome,valor):
        self.nome = nome
        self.valor = valor

c = ''
linhaGlobal = 0
colunaGlobal = 0
lerProxGlobal = True
tabelaSimbolos = {}
def lex():
    state = 'A'
    id = ''
    global c
    global linhaGlobal
    global colunaGlobal
    global tabelaSimbolos
    global lerProxGlobal
    while True:
        match state:
            case 'A':
                if c not in ['\n', '\t', ' ']:
                    id = c
                else:
                    id = ''
                if lerProxGlobal:
                    c = nextChar()
                    id += c
                    colunaGlobal += 1
                else:
                    lerProxGlobal = True
                if c.lower() == 'a':
                    state = 'B'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'D'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'E'
                elif c.lower() == 'f':
                    state = 'F'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'G'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'H'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'I'
                elif c.lower() == 's':
                    state = 'J'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'K'
                elif c.lower() == '-':
                    state = 'L'
                elif c.lower() == '+':
                    state = 'M'
                elif c.lower() == '/':
                    state = 'N'
                elif c.lower() == '*':
                    state = 'O'
                elif c.lower() == '^':
                    state = 'P'
                elif c.lower() == '>':
                    state = 'Q'
                elif c.lower() == '=':
                    state = 'R'
                elif c.lower() == '.':
                    state = 'ER'
                elif c.lower() == ',':
                    state = 'S'
                elif c.lower() == ';':
                    state = 'T'
                elif c.lower() == ':':
                    state = 'RA'
                elif c.lower() == '(':
                    state = 'U'
                elif c.lower() == ')':
                    state = 'V'
                elif c.lower() == '[':
                    state = 'W'
                elif c.lower() == ']':
                    state = 'X'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    colunaGlobal = 0
                    state = 'Y'
                elif c.lower() == '\t':
                    state = 'Y'
                elif c.lower() == ' ':
                    state = 'Y'
                elif c.lower() == '0':
                    state = 'Z'
                elif c.lower() == '1':
                    state = 'Z'
                elif c.lower() == '2':
                    state = 'Z'
                elif c.lower() == '3':
                    state = 'Z'
                elif c.lower() == '4':
                    state = 'Z'
                elif c.lower() == '5':
                    state = 'Z'
                elif c.lower() == '6':
                    state = 'Z'
                elif c.lower() == '7':
                    state = 'Z'
                elif c.lower() == '8':
                    state = 'Z'
                elif c.lower() == '9':
                    state = 'Z'
                elif c.lower() == '$':
                    state = 'DB'
                elif c.lower() == '\'':
                    state = 'AA'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'L':
                #Estado final retorna token '-'
                state = 'A'
                tipo = '-'
                lerProxGlobal = True
                c = ''
                tabelaSimbolos[id.strip()] = Atributo(tipo, id.strip())
                return Token(tipo, id.strip(), linhaGlobal, colunaGlobal)
            case 'M':
                tipo = '+'
                lerProxGlobal = True
                c = ''
                tabelaSimbolos[tipo] = Atributo(tipo, tipo)
                return Token(tipo, tipo, linhaGlobal, colunaGlobal)
            case 'N':
                tipo = '/'
                lerProxGlobal = True
                c = ''
                tabelaSimbolos[tipo] = Atributo(tipo, tipo)
                return Token(tipo, tipo, linhaGlobal, colunaGlobal)
            case 'O':
                tipo = '*'
                lerProxGlobal = True
                c = ''
                tabelaSimbolos[tipo] = Atributo(tipo, tipo)
                return Token(tipo, tipo, linhaGlobal, colunaGlobal)
            case 'P':
                tipo = '^'
                lerProxGlobal = True
                c = ''
                tabelaSimbolos[tipo] = Atributo(tipo, tipo)
                return Token(tipo, tipo, linhaGlobal, colunaGlobal)
            case 'R':
                tipo = 'op_rela'
                lerProxGlobal = True
                c = ''
                tabelaSimbolos[id.strip()] = Atributo(tipo, id.strip())
                return Token(tipo, id.strip(), linhaGlobal, colunaGlobal)
            case 'ER':
                return Token('Erro',id,linhaGlobal,colunaGlobal)
            case 'S':
                tipo = ','
                lerProxGlobal = True
                tabelaSimbolos[id.strip()] = Atributo(tipo, id.strip())
                return Token(tipo, id.strip(), linhaGlobal, colunaGlobal)
            case 'T':
                tipo = ';'
                lerProxGlobal = True
                if id == c:
	                c = ''
	                tabelaSimbolos[id.strip()] = Atributo(tipo, id.strip())
	                return Token(tipo, id.strip(), linhaGlobal, colunaGlobal)
                elif c == '[':
	                state = 'W'
                else:
                    state = 'A'
                    c = ''
                    f.seek(f.tell() + 1)

            case 'RA':
                tipo = ':'
                lerProxGlobal = True
                c = ''
                tabelaSimbolos[tipo] = Atributo(tipo, id.strip())
                return Token(tipo, id.strip(), linhaGlobal, colunaGlobal)
            case 'U':
                tipo = '('
                lerProxGlobal = True
                c = ''
                tabelaSimbolos[id.strip()] = Atributo(tipo, id.strip())
                return Token(tipo, id.strip(), linhaGlobal, colunaGlobal)
            case 'V':
                tipo = ')'
                lerProxGlobal = True
                c = ''
                tabelaSimbolos[id.strip()] = Atributo(tipo, id.strip())
                return Token(tipo, id.strip(), linhaGlobal, colunaGlobal)
            case 'X':
                state = 'A'
                lerProxGlobal = True
            case 'DB':
                tipo = '$'
                lerProxGlobal = True
                tabelaSimbolos[id.strip()] = Atributo(tipo, id.strip())
                return Token(tipo, id.strip(), linhaGlobal, colunaGlobal)
            case 'B':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'AB'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'AC':
                tipo = 'identificador'

                if c != ';':
	                lerProxGlobal = True
	                f.seek(f.tell() - 1)
	                c = ''
                else:
                    lerProxGlobal = False
                tabelaSimbolos[id[:-1].strip()] = Atributo(tipo, id[:-1].strip())
                return Token(tipo, id[:-1].strip(), linhaGlobal, colunaGlobal)

            case 'C':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'D':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'AD'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0

                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'E':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'AE'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'F':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'AF'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'AG'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'AH'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'G':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'AI'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'H':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'AJ'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'I':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'AK'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'J':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'AL'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'K':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'AM'
                elif c.lower() == 'b':
                    state = 'AM'
                elif c.lower() == 'c':
                    state = 'AM'
                elif c.lower() == 'd':
                    state = 'AM'
                elif c.lower() == 'e':
                    state = 'AM'
                elif c.lower() == 'f':
                    state = 'AM'
                elif c.lower() == 'g':
                    state = 'AM'
                elif c.lower() == 'h':
                    state = 'AM'
                elif c.lower() == 'i':
                    state = 'AM'
                elif c.lower() == 'j':
                    state = 'AM'
                elif c.lower() == 'k':
                    state = 'AM'
                elif c.lower() == 'l':
                    state = 'AM'
                elif c.lower() == 'm':
                    state = 'AM'
                elif c.lower() == 'n':
                    state = 'AM'
                elif c.lower() == 'o':
                    state = 'AM'
                elif c.lower() == 'p':
                    state = 'AM'
                elif c.lower() == 'q':
                    state = 'AM'
                elif c.lower() == 'r':
                    state = 'AM'
                elif c.lower() == 's':
                    state = 'AM'
                elif c.lower() == 't':
                    state = 'AM'
                elif c.lower() == 'u':
                    state = 'AM'
                elif c.lower() == 'v':
                    state = 'AM'
                elif c.lower() == 'w':
                    state = 'AM'
                elif c.lower() == 'x':
                    state = 'AM'
                elif c.lower() == 'y':
                    state = 'AM'
                elif c.lower() == 'z':
                    state = 'AM'
                elif c.lower() == '_':
                    state = 'AM'
                elif c.lower() == '<':
                    state = 'AM'
                elif c.lower() == '-':
                    state = 'AN'
                elif c.lower() == '+':
                    state = 'AM'
                elif c.lower() == '/':
                    state = 'AM'
                elif c.lower() == '*':
                    state = 'AM'
                elif c.lower() == '^':
                    state = 'AM'
                elif c.lower() == '>':
                    state = 'AO'
                elif c.lower() == '=':
                    state = 'AP'
                elif c.lower() == '.':
                    state = 'AM'
                elif c.lower() == ',':
                    state = 'AM'
                elif c.lower() == ';':
                    state = 'AM'
                elif c.lower() == ':':
                    state = 'AM'
                elif c.lower() == '(':
                    state = 'AM'
                elif c.lower() == ')':
                    state = 'AM'
                elif c.lower() == '[':
                    state = 'AM'
                elif c.lower() == ']':
                    state = 'AM'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AM'
                elif c.lower() == '\t':
                    state = 'AM'
                elif c.lower() == ' ':
                    state = 'AM'
                elif c.lower() == '0':
                    state = 'AM'
                elif c.lower() == '1':
                    state = 'AM'
                elif c.lower() == '2':
                    state = 'AM'
                elif c.lower() == '3':
                    state = 'AM'
                elif c.lower() == '4':
                    state = 'AM'
                elif c.lower() == '5':
                    state = 'AM'
                elif c.lower() == '6':
                    state = 'AM'
                elif c.lower() == '7':
                    state = 'AM'
                elif c.lower() == '8':
                    state = 'AM'
                elif c.lower() == '9':
                    state = 'AM'
                elif c.lower() == '$':
                    state = 'AM'
                elif c.lower() == '\'':
                    state = 'AM'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'AM':
                tipo = 'op_rela'
                lerProxGlobal = True
                tabelaSimbolos[id[:-1].strip()] = Atributo(tipo, id[:-1].strip())
                return Token(tipo, id[:-1].strip(), linhaGlobal, colunaGlobal)
            case 'AO':
                c = ''
                tabelaSimbolos[id.strip()] = Atributo('op_rela',id.strip())
                return Token('op_rela',id.strip(),linhaGlobal,colunaGlobal)
            case 'AP':
                c = ''
                tabelaSimbolos[id.strip()] = Atributo('op_rela',id.strip())
                return Token('op_rela',id.strip(),linhaGlobal,colunaGlobal)
            case 'Q':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'AQ'
                elif c.lower() == 'b':
                    state = 'AQ'
                elif c.lower() == 'c':
                    state = 'AQ'
                elif c.lower() == 'd':
                    state = 'AQ'
                elif c.lower() == 'e':
                    state = 'AQ'
                elif c.lower() == 'f':
                    state = 'AQ'
                elif c.lower() == 'g':
                    state = 'AQ'
                elif c.lower() == 'h':
                    state = 'AQ'
                elif c.lower() == 'i':
                    state = 'AQ'
                elif c.lower() == 'j':
                    state = 'AQ'
                elif c.lower() == 'k':
                    state = 'AQ'
                elif c.lower() == 'l':
                    state = 'AQ'
                elif c.lower() == 'm':
                    state = 'AQ'
                elif c.lower() == 'n':
                    state = 'AQ'
                elif c.lower() == 'o':
                    state = 'AQ'
                elif c.lower() == 'p':
                    state = 'AQ'
                elif c.lower() == 'q':
                    state = 'AQ'
                elif c.lower() == 'r':
                    state = 'AQ'
                elif c.lower() == 's':
                    state = 'AQ'
                elif c.lower() == 't':
                    state = 'AQ'
                elif c.lower() == 'u':
                    state = 'AQ'
                elif c.lower() == 'v':
                    state = 'AQ'
                elif c.lower() == 'w':
                    state = 'AQ'
                elif c.lower() == 'x':
                    state = 'AQ'
                elif c.lower() == 'y':
                    state = 'AQ'
                elif c.lower() == 'z':
                    state = 'AQ'
                elif c.lower() == '_':
                    state = 'AQ'
                elif c.lower() == '<':
                    state = 'AQ'
                elif c.lower() == '-':
                    state = 'AQ'
                elif c.lower() == '+':
                    state = 'AQ'
                elif c.lower() == '/':
                    state = 'AQ'
                elif c.lower() == '*':
                    state = 'AQ'
                elif c.lower() == '^':
                    state = 'AQ'
                elif c.lower() == '>':
                    state = 'AQ'
                elif c.lower() == '=':
                    state = 'AR'
                elif c.lower() == '.':
                    state = 'AQ'
                elif c.lower() == ',':
                    state = 'AQ'
                elif c.lower() == ';':
                    state = 'AQ'
                elif c.lower() == ':':
                    state = 'AQ'
                elif c.lower() == '(':
                    state = 'AQ'
                elif c.lower() == ')':
                    state = 'AQ'
                elif c.lower() == '[':
                    state = 'AQ'
                elif c.lower() == ']':
                    state = 'AQ'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AQ'
                elif c.lower() == '\t':
                    state = 'AQ'
                elif c.lower() == ' ':
                    state = 'AQ'
                elif c.lower() == '0':
                    state = 'AQ'
                elif c.lower() == '1':
                    state = 'AQ'
                elif c.lower() == '2':
                    state = 'AQ'
                elif c.lower() == '3':
                    state = 'AQ'
                elif c.lower() == '4':
                    state = 'AQ'
                elif c.lower() == '5':
                    state = 'AQ'
                elif c.lower() == '6':
                    state = 'AQ'
                elif c.lower() == '7':
                    state = 'AQ'
                elif c.lower() == '8':
                    state = 'AQ'
                elif c.lower() == '9':
                    state = 'AQ'
                elif c.lower() == '$':
                    state = 'AQ'
                elif c.lower() == '\'':
                    state = 'AQ'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'AQ':
                tipo = 'op_rela'
                lerProxGlobal = True
                tabelaSimbolos[id[:-1].strip()] = Atributo(tipo, id[:-1].strip())
                return Token(tipo, id[:-1].strip(), linhaGlobal, colunaGlobal)
            case 'AR':
                tipo = 'op_rela'
                lerProxGlobal = True
                c = ''
                tabelaSimbolos[id.strip()] = Atributo(tipo,id.strip())
                return Token(tipo,id.strip(),linhaGlobal,colunaGlobal)
            case 'Y':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'AS'
                elif c.lower() == 'b':
                    state = 'AS'
                elif c.lower() == 'c':
                    state = 'AS'
                elif c.lower() == 'd':
                    state = 'AS'
                elif c.lower() == 'e':
                    state = 'AS'
                elif c.lower() == 'f':
                    state = 'AS'
                elif c.lower() == 'g':
                    state = 'AS'
                elif c.lower() == 'h':
                    state = 'AS'
                elif c.lower() == 'i':
                    state = 'AS'
                elif c.lower() == 'j':
                    state = 'AS'
                elif c.lower() == 'k':
                    state = 'AS'
                elif c.lower() == 'l':
                    state = 'AS'
                elif c.lower() == 'm':
                    state = 'AS'
                elif c.lower() == 'n':
                    state = 'AS'
                elif c.lower() == 'o':
                    state = 'AS'
                elif c.lower() == 'p':
                    state = 'AS'
                elif c.lower() == 'q':
                    state = 'AS'
                elif c.lower() == 'r':
                    state = 'AS'
                elif c.lower() == 's':
                    state = 'AS'
                elif c.lower() == 't':
                    state = 'AS'
                elif c.lower() == 'u':
                    state = 'AS'
                elif c.lower() == 'v':
                    state = 'AS'
                elif c.lower() == 'w':
                    state = 'AS'
                elif c.lower() == 'x':
                    state = 'AS'
                elif c.lower() == 'y':
                    state = 'AS'
                elif c.lower() == 'z':
                    state = 'AS'
                elif c.lower() == '_':
                    state = 'AS'
                elif c.lower() == '<':
                    state = 'AS'
                elif c.lower() == '-':
                    state = 'AS'
                elif c.lower() == '+':
                    state = 'AS'
                elif c.lower() == '/':
                    state = 'AS'
                elif c.lower() == '*':
                    state = 'AS'
                elif c.lower() == '^':
                    state = 'AS'
                elif c.lower() == '>':
                    state = 'AS'
                elif c.lower() == '=':
                    state = 'AS'
                elif c.lower() == '.':
                    state = 'AS'
                elif c.lower() == ',':
                    state = 'AS'
                elif c.lower() == ';':
                    state = 'AS'
                elif c.lower() == ':':
                    state = 'AS'
                elif c.lower() == '(':
                    state = 'AS'
                elif c.lower() == ')':
                    state = 'AS'
                elif c.lower() == '[':
                    state = 'AS'
                elif c.lower() == ']':
                    state = 'AS'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'Y'
                elif c.lower() == '\t':
                    state = 'Y'
                elif c.lower() == ' ':
                    state = 'Y'
                elif c.lower() == '0':
                    state = 'AS'
                elif c.lower() == '1':
                    state = 'AS'
                elif c.lower() == '2':
                    state = 'AS'
                elif c.lower() == '3':
                    state = 'AS'
                elif c.lower() == '4':
                    state = 'AS'
                elif c.lower() == '5':
                    state = 'AS'
                elif c.lower() == '6':
                    state = 'AS'
                elif c.lower() == '7':
                    state = 'AS'
                elif c.lower() == '8':
                    state = 'AS'
                elif c.lower() == '9':
                    state = 'AS'
                elif c.lower() == '$':
                    state = 'AS'
                elif c.lower() == '\'':
                    state = 'AS'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'AS':
                state = 'A'
                lerProxGlobal = False
            case 'Z':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'AT'
                elif c.lower() == 'b':
                    state = 'AT'
                elif c.lower() == 'c':
                    state = 'AT'
                elif c.lower() == 'd':
                    state = 'AT'
                elif c.lower() == 'e':
                    state = 'BZ'
                elif c.lower() == 'f':
                    state = 'AT'
                elif c.lower() == 'g':
                    state = 'AT'
                elif c.lower() == 'h':
                    state = 'AT'
                elif c.lower() == 'i':
                    state = 'AT'
                elif c.lower() == 'j':
                    state = 'AT'
                elif c.lower() == 'k':
                    state = 'AT'
                elif c.lower() == 'l':
                    state = 'AT'
                elif c.lower() == 'm':
                    state = 'AT'
                elif c.lower() == 'n':
                    state = 'AT'
                elif c.lower() == 'o':
                    state = 'AT'
                elif c.lower() == 'p':
                    state = 'AT'
                elif c.lower() == 'q':
                    state = 'AT'
                elif c.lower() == 'r':
                    state = 'AT'
                elif c.lower() == 's':
                    state = 'AT'
                elif c.lower() == 't':
                    state = 'AT'
                elif c.lower() == 'u':
                    state = 'AT'
                elif c.lower() == 'v':
                    state = 'AT'
                elif c.lower() == 'w':
                    state = 'AT'
                elif c.lower() == 'x':
                    state = 'AT'
                elif c.lower() == 'y':
                    state = 'AT'
                elif c.lower() == 'z':
                    state = 'AT'
                elif c.lower() == '_':
                    state = 'AT'
                elif c.lower() == '<':
                    state = 'AT'
                elif c.lower() == '-':
                    state = 'AT'
                elif c.lower() == '+':
                    state = 'AT'
                elif c.lower() == '/':
                    state = 'AT'
                elif c.lower() == '*':
                    state = 'AT'
                elif c.lower() == '^':
                    state = 'AT'
                elif c.lower() == '>':
                    state = 'AT'
                elif c.lower() == '=':
                    state = 'AT'
                elif c.lower() == '.':
                    state = 'AU'
                elif c.lower() == ',':
                    state = 'AT'
                elif c.lower() == ';':
                    state = 'AT'
                elif c.lower() == ':':
                    state = 'AT'
                elif c.lower() == '(':
                    state = 'AT'
                elif c.lower() == ')':
                    state = 'AT'
                elif c.lower() == '[':
                    state = 'AT'
                elif c.lower() == ']':
                    state = 'AT'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AT'
                elif c.lower() == '\t':
                    state = 'AT'
                elif c.lower() == ' ':
                    state = 'AT'
                elif c.lower() == '0':
                    state = 'Z'
                elif c.lower() == '1':
                    state = 'Z'
                elif c.lower() == '2':
                    state = 'Z'
                elif c.lower() == '3':
                    state = 'Z'
                elif c.lower() == '4':
                    state = 'Z'
                elif c.lower() == '5':
                    state = 'Z'
                elif c.lower() == '6':
                    state = 'Z'
                elif c.lower() == '7':
                    state = 'Z'
                elif c.lower() == '8':
                    state = 'Z'
                elif c.lower() == '9':
                    state = 'Z'
                elif c.lower() == '$':
                    state = 'AT'
                elif c.lower() == '\'':
                    state = 'AT'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'AT':
                tipo = 'numero'
                lerProxGlobal = True
                f.seek(f.tell() - 1)
                c = ''
                tabelaSimbolos[id[:-1].strip()] = Atributo(tipo, id[:-1].strip())
                return Token(tipo, id[:-1].strip(), linhaGlobal, colunaGlobal)
            case 'AA':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'AV'
                elif c.lower() == 'b':
                    state = 'AV'
                elif c.lower() == 'c':
                    state = 'AV'
                elif c.lower() == 'd':
                    state = 'AV'
                elif c.lower() == 'e':
                    state = 'AV'
                elif c.lower() == 'f':
                    state = 'AV'
                elif c.lower() == 'g':
                    state = 'AV'
                elif c.lower() == 'h':
                    state = 'AV'
                elif c.lower() == 'i':
                    state = 'AV'
                elif c.lower() == 'j':
                    state = 'AV'
                elif c.lower() == 'k':
                    state = 'AV'
                elif c.lower() == 'l':
                    state = 'AV'
                elif c.lower() == 'm':
                    state = 'AV'
                elif c.lower() == 'n':
                    state = 'AV'
                elif c.lower() == 'o':
                    state = 'AV'
                elif c.lower() == 'p':
                    state = 'AV'
                elif c.lower() == 'q':
                    state = 'AV'
                elif c.lower() == 'r':
                    state = 'AV'
                elif c.lower() == 's':
                    state = 'AV'
                elif c.lower() == 't':
                    state = 'AV'
                elif c.lower() == 'u':
                    state = 'AV'
                elif c.lower() == 'v':
                    state = 'AV'
                elif c.lower() == 'w':
                    state = 'AV'
                elif c.lower() == 'x':
                    state = 'AV'
                elif c.lower() == 'y':
                    state = 'AV'
                elif c.lower() == 'z':
                    state = 'AV'
                elif c.lower() == '_':
                    state = 'ER'
                elif c.lower() == '<':
                    state = 'ER'
                elif c.lower() == '-':
                    state = 'ER'
                elif c.lower() == '+':
                    state = 'ER'
                elif c.lower() == '/':
                    state = 'ER'
                elif c.lower() == '*':
                    state = 'ER'
                elif c.lower() == '^':
                    state = 'ER'
                elif c.lower() == '>':
                    state = 'ER'
                elif c.lower() == '=':
                    state = 'ER'
                elif c.lower() == '.':
                    state = 'ER'
                elif c.lower() == ',':
                    state = 'ER'
                elif c.lower() == ';':
                    state = 'ER'
                elif c.lower() == ':':
                    state = 'ER'
                elif c.lower() == '(':
                    state = 'ER'
                elif c.lower() == ')':
                    state = 'ER'
                elif c.lower() == '[':
                    state = 'ER'
                elif c.lower() == ']':
                    state = 'ER'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'ER'
                elif c.lower() == '\t':
                    state = 'ER'
                elif c.lower() == ' ':
                    state = 'ER'
                elif c.lower() == '0':
                    state = 'ER'
                elif c.lower() == '1':
                    state = 'ER'
                elif c.lower() == '2':
                    state = 'ER'
                elif c.lower() == '3':
                    state = 'ER'
                elif c.lower() == '4':
                    state = 'ER'
                elif c.lower() == '5':
                    state = 'ER'
                elif c.lower() == '6':
                    state = 'ER'
                elif c.lower() == '7':
                    state = 'ER'
                elif c.lower() == '8':
                    state = 'ER'
                elif c.lower() == '9':
                    state = 'ER'
                elif c.lower() == '$':
                    state = 'ER'
                elif c.lower() == '\'':
                    state = 'ER'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'AB':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'AW'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'AD':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'AY'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'AE':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'AY'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'AX'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'AZ'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'AF':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'BA'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'AG':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'BB'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'AH':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'BC'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'AI':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'BD'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'BE'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'AJ':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'BF'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'AK':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'BG'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'AL':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'BH'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'BI'
                elif c.lower() == '-':
                    state = 'BI'
                elif c.lower() == '+':
                    state = 'BI'
                elif c.lower() == '/':
                    state = 'BI'
                elif c.lower() == '*':
                    state = 'BI'
                elif c.lower() == '^':
                    state = 'BI'
                elif c.lower() == '>':
                    state = 'BI'
                elif c.lower() == '=':
                    state = 'BI'
                elif c.lower() == '.':
                    state = 'BI'
                elif c.lower() == ',':
                    state = 'BI'
                elif c.lower() == ';':
                    state = 'BI'
                elif c.lower() == ':':
                    state = 'BI'
                elif c.lower() == '(':
                    state = 'BI'
                elif c.lower() == ')':
                    state = 'BI'
                elif c.lower() == '[':
                    state = 'BI'
                elif c.lower() == ']':
                    state = 'BI'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'BI'
                elif c.lower() == '\t':
                    state = 'BI'
                elif c.lower() == ' ':
                    state = 'BI'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'BI'
                elif c.lower() == '\'':
                    state = 'BI'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'BI':
                tipo = 'se'
                lerProxGlobal = True
                f.seek(f.tell() - 1)
                c = ''
                tabelaSimbolos[id[:-1].strip()] = Atributo(tipo, id[:-1].strip())
                return Token(tipo, id[:-1].strip(), linhaGlobal, colunaGlobal)
            case 'AN':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == '-':
                    state = 'BJ'
                else:
                    state = 'A'
                    lerProxGlobal = False
                    tipo = 'op_rela' if id in ['=','<','>','<>','<=','>=','='] else ('op_arit' if id in ['+','-','*','/','^'] else ( id.strip() if id.strip() in ['se','senao','entao','ate','enquanto', 'programa', 'inicio', 'fim','faca','repita'] else ('numero' if re.search('[0-9]([0-9]?)(.[0-9]([0-9]*)?)?([Ee][+-]?[0-9]([0-9])*)?',id.strip()) else ('identificador' if re.search('([a-zA-Z_]+)([a-zA-Z0-9_])*',id.strip()) else ''))))
                    if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
                        f.seek(f.tell()-1)
                        tabelaSimbolos[id[:-1].strip()] = Atributo(tipo,id[:-1].strip())
                        return Token(tipo,id[:-1].strip(),linhaGlobal,colunaGlobal)
                    elif c in ['\n', '\t', ' ',';',')','+']:
                        tabelaSimbolos[id] = Atributo(tipo,id)
                        return Token(tipo,id,linhaGlobal,colunaGlobal)
                    else:
                        tabelaSimbolos[id.strip()] = Atributo(tipo,id.strip())
                        return Token(tipo,id.strip(),linhaGlobal,colunaGlobal)
            case 'AU':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'ER'
                elif c.lower() == 'b':
                    state = 'ER'
                elif c.lower() == 'c':
                    state = 'ER'
                elif c.lower() == 'd':
                    state = 'ER'
                elif c.lower() == 'e':
                    state = 'ER'
                elif c.lower() == 'f':
                    state = 'ER'
                elif c.lower() == 'g':
                    state = 'ER'
                elif c.lower() == 'h':
                    state = 'ER'
                elif c.lower() == 'i':
                    state = 'ER'
                elif c.lower() == 'j':
                    state = 'ER'
                elif c.lower() == 'k':
                    state = 'ER'
                elif c.lower() == 'l':
                    state = 'ER'
                elif c.lower() == 'm':
                    state = 'ER'
                elif c.lower() == 'n':
                    state = 'ER'
                elif c.lower() == 'o':
                    state = 'ER'
                elif c.lower() == 'p':
                    state = 'ER'
                elif c.lower() == 'q':
                    state = 'ER'
                elif c.lower() == 'r':
                    state = 'ER'
                elif c.lower() == 's':
                    state = 'ER'
                elif c.lower() == 't':
                    state = 'ER'
                elif c.lower() == 'u':
                    state = 'ER'
                elif c.lower() == 'v':
                    state = 'ER'
                elif c.lower() == 'w':
                    state = 'ER'
                elif c.lower() == 'x':
                    state = 'ER'
                elif c.lower() == 'y':
                    state = 'ER'
                elif c.lower() == 'z':
                    state = 'ER'
                elif c.lower() == '_':
                    state = 'ER'
                elif c.lower() == '<':
                    state = 'ER'
                elif c.lower() == '-':
                    state = 'ER'
                elif c.lower() == '+':
                    state = 'ER'
                elif c.lower() == '/':
                    state = 'ER'
                elif c.lower() == '*':
                    state = 'ER'
                elif c.lower() == '^':
                    state = 'ER'
                elif c.lower() == '>':
                    state = 'ER'
                elif c.lower() == '=':
                    state = 'ER'
                elif c.lower() == '.':
                    state = 'ER'
                elif c.lower() == ',':
                    state = 'ER'
                elif c.lower() == ';':
                    state = 'ER'
                elif c.lower() == ':':
                    state = 'ER'
                elif c.lower() == '(':
                    state = 'ER'
                elif c.lower() == ')':
                    state = 'ER'
                elif c.lower() == '[':
                    state = 'ER'
                elif c.lower() == ']':
                    state = 'ER'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'ER'
                elif c.lower() == '\t':
                    state = 'ER'
                elif c.lower() == ' ':
                    state = 'ER'
                elif c.lower() == '0':
                    state = 'BK'
                elif c.lower() == '1':
                    state = 'BK'
                elif c.lower() == '2':
                    state = 'BK'
                elif c.lower() == '3':
                    state = 'BK'
                elif c.lower() == '4':
                    state = 'BK'
                elif c.lower() == '5':
                    state = 'BK'
                elif c.lower() == '6':
                    state = 'BK'
                elif c.lower() == '7':
                    state = 'BK'
                elif c.lower() == '8':
                    state = 'BK'
                elif c.lower() == '9':
                    state = 'BK'
                elif c.lower() == '$':
                    state = 'ER'
                elif c.lower() == '\'':
                    state = 'ER'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'AV':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'ER'
                elif c.lower() == 'b':
                    state = 'ER'
                elif c.lower() == 'c':
                    state = 'ER'
                elif c.lower() == 'd':
                    state = 'ER'
                elif c.lower() == 'e':
                    state = 'ER'
                elif c.lower() == 'f':
                    state = 'ER'
                elif c.lower() == 'g':
                    state = 'ER'
                elif c.lower() == 'h':
                    state = 'ER'
                elif c.lower() == 'i':
                    state = 'ER'
                elif c.lower() == 'j':
                    state = 'ER'
                elif c.lower() == 'k':
                    state = 'ER'
                elif c.lower() == 'l':
                    state = 'ER'
                elif c.lower() == 'm':
                    state = 'ER'
                elif c.lower() == 'n':
                    state = 'ER'
                elif c.lower() == 'o':
                    state = 'ER'
                elif c.lower() == 'p':
                    state = 'ER'
                elif c.lower() == 'q':
                    state = 'ER'
                elif c.lower() == 'r':
                    state = 'ER'
                elif c.lower() == 's':
                    state = 'ER'
                elif c.lower() == 't':
                    state = 'ER'
                elif c.lower() == 'u':
                    state = 'ER'
                elif c.lower() == 'v':
                    state = 'ER'
                elif c.lower() == 'w':
                    state = 'ER'
                elif c.lower() == 'x':
                    state = 'ER'
                elif c.lower() == 'y':
                    state = 'ER'
                elif c.lower() == 'z':
                    state = 'ER'
                elif c.lower() == '_':
                    state = 'ER'
                elif c.lower() == '<':
                    state = 'ER'
                elif c.lower() == '-':
                    state = 'ER'
                elif c.lower() == '+':
                    state = 'ER'
                elif c.lower() == '/':
                    state = 'ER'
                elif c.lower() == '*':
                    state = 'ER'
                elif c.lower() == '^':
                    state = 'ER'
                elif c.lower() == '>':
                    state = 'ER'
                elif c.lower() == '=':
                    state = 'ER'
                elif c.lower() == '.':
                    state = 'ER'
                elif c.lower() == ',':
                    state = 'ER'
                elif c.lower() == ';':
                    state = 'ER'
                elif c.lower() == ':':
                    state = 'ER'
                elif c.lower() == '(':
                    state = 'ER'
                elif c.lower() == ')':
                    state = 'ER'
                elif c.lower() == '[':
                    state = 'ER'
                elif c.lower() == ']':
                    state = 'ER'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'ER'
                elif c.lower() == '\t':
                    state = 'ER'
                elif c.lower() == ' ':
                    state = 'ER'
                elif c.lower() == '0':
                    state = 'ER'
                elif c.lower() == '1':
                    state = 'ER'
                elif c.lower() == '2':
                    state = 'ER'
                elif c.lower() == '3':
                    state = 'ER'
                elif c.lower() == '4':
                    state = 'ER'
                elif c.lower() == '5':
                    state = 'ER'
                elif c.lower() == '6':
                    state = 'ER'
                elif c.lower() == '7':
                    state = 'ER'
                elif c.lower() == '8':
                    state = 'ER'
                elif c.lower() == '9':
                    state = 'ER'
                elif c.lower() == '$':
                    state = 'BL'
                elif c.lower() == '\'':
                    state = 'BL'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'BL':
                tipo = 'letra'
                lerProxGlobal = True
                tabelaSimbolos[id.strip()] = Atributo(tipo,id.strip())
                return Token(tipo,id.strip(),linhaGlobal,colunaGlobal)
            case 'AW':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'BM'
                elif c.lower() == '-':
                    state = 'BM'
                elif c.lower() == '+':
                    state = 'BM'
                elif c.lower() == '/':
                    state = 'BM'
                elif c.lower() == '*':
                    state = 'BM'
                elif c.lower() == '^':
                    state = 'BM'
                elif c.lower() == '>':
                    state = 'BM'
                elif c.lower() == '=':
                    state = 'BM'
                elif c.lower() == '.':
                    state = 'BM'
                elif c.lower() == ',':
                    state = 'BM'
                elif c.lower() == ';':
                    state = 'BM'
                elif c.lower() == ':':
                    state = 'BM'
                elif c.lower() == '(':
                    state = 'BM'
                elif c.lower() == ')':
                    state = 'BM'
                elif c.lower() == '[':
                    state = 'BM'
                elif c.lower() == ']':
                    state = 'BM'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'BM'
                elif c.lower() == '\t':
                    state = 'BM'
                elif c.lower() == ' ':
                    state = 'BM'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'BM'
                elif c.lower() == '\'':
                    state = 'BM'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'BM':
                tipo = 'ate'
                lerProxGlobal = True
                f.seek(f.tell() - 1)
                c = ''
                tabelaSimbolos[id[:-1].strip()] = Atributo(tipo, id[:-1].strip())
                return Token(tipo, id[:-1].strip(), linhaGlobal, colunaGlobal)
            case 'AY':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'BN'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'AX':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'BO'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'AZ':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'AZZ'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'AZZ':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'BP'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'BA':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'BQ'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'BB':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'BR'
                elif c.lower() == '-':
                    state = 'BR'
                elif c.lower() == '+':
                    state = 'BR'
                elif c.lower() == '/':
                    state = 'BR'
                elif c.lower() == '*':
                    state = 'BR'
                elif c.lower() == '^':
                    state = 'BR'
                elif c.lower() == '>':
                    state = 'BR'
                elif c.lower() == '=':
                    state = 'BR'
                elif c.lower() == '.':
                    state = 'BR'
                elif c.lower() == ',':
                    state = 'BR'
                elif c.lower() == ';':
                    state = 'BR'
                elif c.lower() == ':':
                    state = 'BR'
                elif c.lower() == '(':
                    state = 'BR'
                elif c.lower() == ')':
                    state = 'BR'
                elif c.lower() == '[':
                    state = 'BR'
                elif c.lower() == ']':
                    state = 'BR'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'BR'
                elif c.lower() == '\t':
                    state = 'BR'
                elif c.lower() == ' ':
                    state = 'BR'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'BR'
                elif c.lower() == '\'':
                    state = 'BR'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'BR':
                tipo = 'fim'
                lerProxGlobal = True
                tabelaSimbolos[tipo] = Atributo(tipo, tipo)
                return Token(tipo, tipo, linhaGlobal, colunaGlobal)
            case 'BC':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'BS'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'BD':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'BT'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'BE':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'BU'
                elif c.lower() == '-':
                    state = 'BU'
                elif c.lower() == '+':
                    state = 'BU'
                elif c.lower() == '/':
                    state = 'BU'
                elif c.lower() == '*':
                    state = 'BU'
                elif c.lower() == '^':
                    state = 'BU'
                elif c.lower() == '>':
                    state = 'BU'
                elif c.lower() == '=':
                    state = 'BU'
                elif c.lower() == '.':
                    state = 'BU'
                elif c.lower() == ',':
                    state = 'BU'
                elif c.lower() == ';':
                    state = 'BU'
                elif c.lower() == ':':
                    state = 'BU'
                elif c.lower() == '(':
                    state = 'BU'
                elif c.lower() == ')':
                    state = 'BU'
                elif c.lower() == '[':
                    state = 'BU'
                elif c.lower() == ']':
                    state = 'BU'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'BU'
                elif c.lower() == '\t':
                    state = 'BU'
                elif c.lower() == ' ':
                    state = 'BU'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'BU'
                elif c.lower() == '\'':
                    state = 'BU'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'BU':
                state = 'A'
                tipo = 'tipo'
                lerProxGlobal = True
                f.seek(f.tell() - 1)
                c = ''
                tabelaSimbolos[id[:-1].strip()] = Atributo(tipo, id[:-1].strip())
                return Token(tipo, id[:-1].strip(), linhaGlobal, colunaGlobal)
            case 'BF':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'BV'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'BG':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'BW'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'BH':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'BX'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'BJ':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'BY'
                elif c.lower() == 'b':
                    state = 'BY'
                elif c.lower() == 'c':
                    state = 'BY'
                elif c.lower() == 'd':
                    state = 'BY'
                elif c.lower() == 'e':
                    state = 'BY'
                elif c.lower() == 'f':
                    state = 'BY'
                elif c.lower() == 'g':
                    state = 'BY'
                elif c.lower() == 'h':
                    state = 'BY'
                elif c.lower() == 'i':
                    state = 'BY'
                elif c.lower() == 'j':
                    state = 'BY'
                elif c.lower() == 'k':
                    state = 'BY'
                elif c.lower() == 'l':
                    state = 'BY'
                elif c.lower() == 'm':
                    state = 'BY'
                elif c.lower() == 'n':
                    state = 'BY'
                elif c.lower() == 'o':
                    state = 'BY'
                elif c.lower() == 'p':
                    state = 'BY'
                elif c.lower() == 'q':
                    state = 'BY'
                elif c.lower() == 'r':
                    state = 'BY'
                elif c.lower() == 's':
                    state = 'BY'
                elif c.lower() == 't':
                    state = 'BY'
                elif c.lower() == 'u':
                    state = 'BY'
                elif c.lower() == 'v':
                    state = 'BY'
                elif c.lower() == 'w':
                    state = 'BY'
                elif c.lower() == 'x':
                    state = 'BY'
                elif c.lower() == 'y':
                    state = 'BY'
                elif c.lower() == 'z':
                    state = 'BY'
                elif c.lower() == '_':
                    state = 'BY'
                elif c.lower() == '<':
                    state = 'BY'
                elif c.lower() == '-':
                    state = 'BY'
                elif c.lower() == '+':
                    state = 'BY'
                elif c.lower() == '/':
                    state = 'BY'
                elif c.lower() == '*':
                    state = 'BY'
                elif c.lower() == '^':
                    state = 'BY'
                elif c.lower() == '>':
                    state = 'BY'
                elif c.lower() == '=':
                    state = 'BY'
                elif c.lower() == '.':
                    state = 'BY'
                elif c.lower() == ',':
                    state = 'BY'
                elif c.lower() == ';':
                    state = 'BY'
                elif c.lower() == ':':
                    state = 'BY'
                elif c.lower() == '(':
                    state = 'BY'
                elif c.lower() == ')':
                    state = 'BY'
                elif c.lower() == '[':
                    state = 'BY'
                elif c.lower() == ']':
                    state = 'BY'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'BY'
                elif c.lower() == '\t':
                    state = 'BY'
                elif c.lower() == ' ':
                    state = 'BY'
                elif c.lower() == '0':
                    state = 'BY'
                elif c.lower() == '1':
                    state = 'BY'
                elif c.lower() == '2':
                    state = 'BY'
                elif c.lower() == '3':
                    state = 'BY'
                elif c.lower() == '4':
                    state = 'BY'
                elif c.lower() == '5':
                    state = 'BY'
                elif c.lower() == '6':
                    state = 'BY'
                elif c.lower() == '7':
                    state = 'BY'
                elif c.lower() == '8':
                    state = 'BY'
                elif c.lower() == '9':
                    state = 'BY'
                elif c.lower() == '$':
                    state = 'BY'
                elif c.lower() == '\'':
                    state = 'BY'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'BY':
                tipo = '<--'
                lerProxGlobal = True
                f.seek(f.tell() - 1)
                c = ''
                tabelaSimbolos[id[:-1].strip()] = Atributo(tipo, id[:-1].strip())
                return Token(tipo, id[:-1].strip(), linhaGlobal, colunaGlobal)
            case 'BK':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'CA'
                elif c.lower() == 'b':
                    state = 'CA'
                elif c.lower() == 'c':
                    state = 'CA'
                elif c.lower() == 'd':
                    state = 'CA'
                elif c.lower() == 'e':
                    state = 'BZ'
                elif c.lower() == 'f':
                    state = 'CA'
                elif c.lower() == 'g':
                    state = 'CA'
                elif c.lower() == 'h':
                    state = 'CA'
                elif c.lower() == 'i':
                    state = 'CA'
                elif c.lower() == 'j':
                    state = 'CA'
                elif c.lower() == 'k':
                    state = 'CA'
                elif c.lower() == 'l':
                    state = 'CA'
                elif c.lower() == 'm':
                    state = 'CA'
                elif c.lower() == 'n':
                    state = 'CA'
                elif c.lower() == 'o':
                    state = 'CA'
                elif c.lower() == 'p':
                    state = 'CA'
                elif c.lower() == 'q':
                    state = 'CA'
                elif c.lower() == 'r':
                    state = 'CA'
                elif c.lower() == 's':
                    state = 'CA'
                elif c.lower() == 't':
                    state = 'CA'
                elif c.lower() == 'u':
                    state = 'CA'
                elif c.lower() == 'v':
                    state = 'CA'
                elif c.lower() == 'w':
                    state = 'CA'
                elif c.lower() == 'x':
                    state = 'CA'
                elif c.lower() == 'y':
                    state = 'CA'
                elif c.lower() == 'z':
                    state = 'CA'
                elif c.lower() == '_':
                    state = 'CA'
                elif c.lower() == '<':
                    state = 'CA'
                elif c.lower() == '-':
                    state = 'CA'
                elif c.lower() == '+':
                    state = 'CA'
                elif c.lower() == '/':
                    state = 'CA'
                elif c.lower() == '*':
                    state = 'CA'
                elif c.lower() == '^':
                    state = 'CA'
                elif c.lower() == '>':
                    state = 'CA'
                elif c.lower() == '=':
                    state = 'CA'
                elif c.lower() == '.':
                    state = 'CA'
                elif c.lower() == ',':
                    state = 'CA'
                elif c.lower() == ';':
                    state = 'CA'
                elif c.lower() == ':':
                    state = 'CA'
                elif c.lower() == '(':
                    state = 'CA'
                elif c.lower() == ')':
                    state = 'CA'
                elif c.lower() == '[':
                    state = 'CA'
                elif c.lower() == ']':
                    state = 'CA'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'CA'
                elif c.lower() == '\t':
                    state = 'CA'
                elif c.lower() == ' ':
                    state = 'CA'
                elif c.lower() == '0':
                    state = 'BK'
                elif c.lower() == '1':
                    state = 'BK'
                elif c.lower() == '2':
                    state = 'BK'
                elif c.lower() == '3':
                    state = 'BK'
                elif c.lower() == '4':
                    state = 'BK'
                elif c.lower() == '5':
                    state = 'BK'
                elif c.lower() == '6':
                    state = 'BK'
                elif c.lower() == '7':
                    state = 'BK'
                elif c.lower() == '8':
                    state = 'BK'
                elif c.lower() == '9':
                    state = 'BK'
                elif c.lower() == '$':
                    state = 'CA'
                elif c.lower() == '\'':
                    state = 'CA'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'CA':
                tipo = 'numero'
                lerProxGlobal = True
                if c == ')':
	                c = ''
                elif c == ';':
	                lerProxGlobal = False
                f.seek(f.tell() - 1)
                tabelaSimbolos[id[:-1].strip()] = Atributo(tipo, id[:-1].strip())
                return Token(tipo, id[:-1].strip(), linhaGlobal, colunaGlobal)
            case 'BM':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'BN':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'CB'
                elif c.lower() == '-':
                    state = 'CB'
                elif c.lower() == '+':
                    state = 'CB'
                elif c.lower() == '/':
                    state = 'CB'
                elif c.lower() == '*':
                    state = 'CB'
                elif c.lower() == '^':
                    state = 'CB'
                elif c.lower() == '>':
                    state = 'CB'
                elif c.lower() == '=':
                    state = 'CB'
                elif c.lower() == '.':
                    state = 'CB'
                elif c.lower() == ',':
                    state = 'CB'
                elif c.lower() == ';':
                    state = 'CB'
                elif c.lower() == ':':
                    state = 'CB'
                elif c.lower() == '(':
                    state = 'CB'
                elif c.lower() == ')':
                    state = 'CB'
                elif c.lower() == '[':
                    state = 'CB'
                elif c.lower() == ']':
                    state = 'CB'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'CB'
                elif c.lower() == '\t':
                    state = 'CB'
                elif c.lower() == ' ':
                    state = 'CB'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'CB'
                elif c.lower() == '\'':
                    state = 'CB'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'CB':
                state = 'A'
                tipo = 'tipo'
                lerProxGlobal = True
                f.seek(f.tell() - 1)
                c = ''
                tabelaSimbolos[id[:-1].strip()] = Atributo(tipo, id[:-1].strip())
                return Token(tipo, id[:-1].strip(), linhaGlobal, colunaGlobal)

            case 'BO':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'CC'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'BP':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'CD'
                elif c.lower() == '-':
                    state = 'CD'
                elif c.lower() == '+':
                    state = 'CD'
                elif c.lower() == '/':
                    state = 'CD'
                elif c.lower() == '*':
                    state = 'CD'
                elif c.lower() == '^':
                    state = 'CD'
                elif c.lower() == '>':
                    state = 'CD'
                elif c.lower() == '=':
                    state = 'CD'
                elif c.lower() == '.':
                    state = 'CD'
                elif c.lower() == ',':
                    state = 'CD'
                elif c.lower() == ';':
                    state = 'CD'
                elif c.lower() == ':':
                    state = 'CD'
                elif c.lower() == '(':
                    state = 'CD'
                elif c.lower() == ')':
                    state = 'CD'
                elif c.lower() == '[':
                    state = 'CD'
                elif c.lower() == ']':
                    state = 'CD'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'CD'
                elif c.lower() == '\t':
                    state = 'CD'
                elif c.lower() == ' ':
                    state = 'CD'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'CD'
                elif c.lower() == '\'':
                    state = 'CD'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'CD':
                tipo = 'entao'
                lerProxGlobal = True
                f.seek(f.tell() - 1)
                c = ''
                tabelaSimbolos[id[:-1].strip()] = Atributo(tipo, id[:-1].strip())
                return Token(tipo, id[:-1].strip(), linhaGlobal, colunaGlobal)
            case 'BQ':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'CE'
                elif c.lower() == '-':
                    state = 'CE'
                elif c.lower() == '+':
                    state = 'CE'
                elif c.lower() == '/':
                    state = 'CE'
                elif c.lower() == '*':
                    state = 'CE'
                elif c.lower() == '^':
                    state = 'CE'
                elif c.lower() == '>':
                    state = 'CE'
                elif c.lower() == '=':
                    state = 'CE'
                elif c.lower() == '.':
                    state = 'CE'
                elif c.lower() == ',':
                    state = 'CE'
                elif c.lower() == ';':
                    state = 'CE'
                elif c.lower() == ':':
                    state = 'CE'
                elif c.lower() == '(':
                    state = 'CE'
                elif c.lower() == ')':
                    state = 'CE'
                elif c.lower() == '[':
                    state = 'CE'
                elif c.lower() == ']':
                    state = 'CE'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'CE'
                elif c.lower() == '\t':
                    state = 'CE'
                elif c.lower() == ' ':
                    state = 'CE'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'CE'
                elif c.lower() == '\'':
                    state = 'CE'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'CE':
                tipo = 'faca'
                lerProxGlobal = True
                f.seek(f.tell() - 1)
                c = ''
                tabelaSimbolos[id[:-1].strip()] = Atributo(tipo, id[:-1].strip())
                return Token(tipo, id[:-1].strip(), linhaGlobal, colunaGlobal)
            case 'BS':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'CF'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'BT':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'CG'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'BV':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'CH'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'BW':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'CI'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'BX':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'CJ'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'BZ':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'ER'
                elif c.lower() == 'b':
                    state = 'ER'
                elif c.lower() == 'c':
                    state = 'ER'
                elif c.lower() == 'd':
                    state = 'ER'
                elif c.lower() == 'e':
                    state = 'ER'
                elif c.lower() == 'f':
                    state = 'ER'
                elif c.lower() == 'g':
                    state = 'ER'
                elif c.lower() == 'h':
                    state = 'ER'
                elif c.lower() == 'i':
                    state = 'ER'
                elif c.lower() == 'j':
                    state = 'ER'
                elif c.lower() == 'k':
                    state = 'ER'
                elif c.lower() == 'l':
                    state = 'ER'
                elif c.lower() == 'm':
                    state = 'ER'
                elif c.lower() == 'n':
                    state = 'ER'
                elif c.lower() == 'o':
                    state = 'ER'
                elif c.lower() == 'p':
                    state = 'ER'
                elif c.lower() == 'q':
                    state = 'ER'
                elif c.lower() == 'r':
                    state = 'ER'
                elif c.lower() == 's':
                    state = 'ER'
                elif c.lower() == 't':
                    state = 'ER'
                elif c.lower() == 'u':
                    state = 'ER'
                elif c.lower() == 'v':
                    state = 'ER'
                elif c.lower() == 'w':
                    state = 'ER'
                elif c.lower() == 'x':
                    state = 'ER'
                elif c.lower() == 'y':
                    state = 'ER'
                elif c.lower() == 'z':
                    state = 'ER'
                elif c.lower() == '_':
                    state = 'ER'
                elif c.lower() == '<':
                    state = 'ER'
                elif c.lower() == '-':
                    state = 'CK'
                elif c.lower() == '+':
                    state = 'CK'
                elif c.lower() == '/':
                    state = 'ER'
                elif c.lower() == '*':
                    state = 'ER'
                elif c.lower() == '^':
                    state = 'ER'
                elif c.lower() == '>':
                    state = 'ER'
                elif c.lower() == '=':
                    state = 'ER'
                elif c.lower() == '.':
                    state = 'ER'
                elif c.lower() == ',':
                    state = 'ER'
                elif c.lower() == ';':
                    state = 'ER'
                elif c.lower() == ':':
                    state = 'ER'
                elif c.lower() == '(':
                    state = 'ER'
                elif c.lower() == ')':
                    state = 'ER'
                elif c.lower() == '[':
                    state = 'ER'
                elif c.lower() == ']':
                    state = 'ER'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'ER'
                elif c.lower() == '\t':
                    state = 'ER'
                elif c.lower() == ' ':
                    state = 'ER'
                elif c.lower() == '0':
                    state = 'CL'
                elif c.lower() == '1':
                    state = 'CL'
                elif c.lower() == '2':
                    state = 'CL'
                elif c.lower() == '3':
                    state = 'CL'
                elif c.lower() == '4':
                    state = 'CL'
                elif c.lower() == '5':
                    state = 'CL'
                elif c.lower() == '6':
                    state = 'CL'
                elif c.lower() == '7':
                    state = 'CL'
                elif c.lower() == '8':
                    state = 'CL'
                elif c.lower() == '9':
                    state = 'CL'
                elif c.lower() == '$':
                    state = 'ER'
                elif c.lower() == '\'':
                    state = 'ER'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'CC':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'CM'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'CF':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'CN'
                elif c.lower() == '-':
                    state = 'CN'
                elif c.lower() == '+':
                    state = 'CN'
                elif c.lower() == '/':
                    state = 'CN'
                elif c.lower() == '*':
                    state = 'CN'
                elif c.lower() == '^':
                    state = 'CN'
                elif c.lower() == '>':
                    state = 'CN'
                elif c.lower() == '=':
                    state = 'CN'
                elif c.lower() == '.':
                    state = 'CN'
                elif c.lower() == ',':
                    state = 'CN'
                elif c.lower() == ';':
                    state = 'CN'
                elif c.lower() == ':':
                    state = 'CN'
                elif c.lower() == '(':
                    state = 'CN'
                elif c.lower() == ')':
                    state = 'CN'
                elif c.lower() == '[':
                    state = 'CN'
                elif c.lower() == ']':
                    state = 'CN'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'CN'
                elif c.lower() == '\t':
                    state = 'CN'
                elif c.lower() == ' ':
                    state = 'CN'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'CN'
                elif c.lower() == '\'':
                    state = 'CN'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'CN':
                state = 'A'
                tipo = 'tipo'
                lerProxGlobal = True
                f.seek(f.tell() - 1)
                c = ''
                tabelaSimbolos[id[:-1].strip()] = Atributo(tipo, id[:-1].strip())
                return Token(tipo, id[:-1].strip(), linhaGlobal, colunaGlobal)

            case 'CG':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'CO'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'CH':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'CP'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'CI':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'CQ'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'CJ':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'CR'
                elif c.lower() == '-':
                    state = 'CR'
                elif c.lower() == '+':
                    state = 'CR'
                elif c.lower() == '/':
                    state = 'CR'
                elif c.lower() == '*':
                    state = 'CR'
                elif c.lower() == '^':
                    state = 'CR'
                elif c.lower() == '>':
                    state = 'CR'
                elif c.lower() == '=':
                    state = 'CR'
                elif c.lower() == '.':
                    state = 'CR'
                elif c.lower() == ',':
                    state = 'CR'
                elif c.lower() == ';':
                    state = 'CR'
                elif c.lower() == ':':
                    state = 'CR'
                elif c.lower() == '(':
                    state = 'CR'
                elif c.lower() == ')':
                    state = 'CR'
                elif c.lower() == '[':
                    state = 'CR'
                elif c.lower() == ']':
                    state = 'CR'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'CR'
                elif c.lower() == '\t':
                    state = 'CR'
                elif c.lower() == ' ':
                    state = 'CR'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'CR'
                elif c.lower() == '\'':
                    state = 'CR'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'CR':
                tipo = 'senao'
                lerProxGlobal = False
                tabelaSimbolos[id[:-1].strip()] = Atributo(tipo, id[:-1].strip())
                return Token(tipo, id[:-1].strip(), linhaGlobal, colunaGlobal)

            case 'CK':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'ER'
                elif c.lower() == 'b':
                    state = 'ER'
                elif c.lower() == 'c':
                    state = 'ER'
                elif c.lower() == 'd':
                    state = 'ER'
                elif c.lower() == 'e':
                    state = 'ER'
                elif c.lower() == 'f':
                    state = 'ER'
                elif c.lower() == 'g':
                    state = 'ER'
                elif c.lower() == 'h':
                    state = 'ER'
                elif c.lower() == 'i':
                    state = 'ER'
                elif c.lower() == 'j':
                    state = 'ER'
                elif c.lower() == 'k':
                    state = 'ER'
                elif c.lower() == 'l':
                    state = 'ER'
                elif c.lower() == 'm':
                    state = 'ER'
                elif c.lower() == 'n':
                    state = 'ER'
                elif c.lower() == 'o':
                    state = 'ER'
                elif c.lower() == 'p':
                    state = 'ER'
                elif c.lower() == 'q':
                    state = 'ER'
                elif c.lower() == 'r':
                    state = 'ER'
                elif c.lower() == 's':
                    state = 'ER'
                elif c.lower() == 't':
                    state = 'ER'
                elif c.lower() == 'u':
                    state = 'ER'
                elif c.lower() == 'v':
                    state = 'ER'
                elif c.lower() == 'w':
                    state = 'ER'
                elif c.lower() == 'x':
                    state = 'ER'
                elif c.lower() == 'y':
                    state = 'ER'
                elif c.lower() == 'z':
                    state = 'ER'
                elif c.lower() == '_':
                    state = 'ER'
                elif c.lower() == '<':
                    state = 'ER'
                elif c.lower() == '-':
                    state = 'ER'
                elif c.lower() == '+':
                    state = 'ER'
                elif c.lower() == '/':
                    state = 'ER'
                elif c.lower() == '*':
                    state = 'ER'
                elif c.lower() == '^':
                    state = 'ER'
                elif c.lower() == '>':
                    state = 'ER'
                elif c.lower() == '=':
                    state = 'ER'
                elif c.lower() == '.':
                    state = 'ER'
                elif c.lower() == ',':
                    state = 'ER'
                elif c.lower() == ';':
                    state = 'ER'
                elif c.lower() == ':':
                    state = 'ER'
                elif c.lower() == '(':
                    state = 'ER'
                elif c.lower() == ')':
                    state = 'ER'
                elif c.lower() == '[':
                    state = 'ER'
                elif c.lower() == ']':
                    state = 'ER'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'ER'
                elif c.lower() == '\t':
                    state = 'ER'
                elif c.lower() == ' ':
                    state = 'ER'
                elif c.lower() == '0':
                    state = 'CL'
                elif c.lower() == '1':
                    state = 'CL'
                elif c.lower() == '2':
                    state = 'CL'
                elif c.lower() == '3':
                    state = 'CL'
                elif c.lower() == '4':
                    state = 'CL'
                elif c.lower() == '5':
                    state = 'CL'
                elif c.lower() == '6':
                    state = 'CL'
                elif c.lower() == '7':
                    state = 'CL'
                elif c.lower() == '8':
                    state = 'CL'
                elif c.lower() == '9':
                    state = 'CL'
                elif c.lower() == '$':
                    state = 'ER'
                elif c.lower() == '\'':
                    state = 'ER'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'CL':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'CS'
                elif c.lower() == 'b':
                    state = 'CS'
                elif c.lower() == 'c':
                    state = 'CS'
                elif c.lower() == 'd':
                    state = 'CS'
                elif c.lower() == 'e':
                    state = 'CS'
                elif c.lower() == 'f':
                    state = 'CS'
                elif c.lower() == 'g':
                    state = 'CS'
                elif c.lower() == 'h':
                    state = 'CS'
                elif c.lower() == 'i':
                    state = 'CS'
                elif c.lower() == 'j':
                    state = 'CS'
                elif c.lower() == 'k':
                    state = 'CS'
                elif c.lower() == 'l':
                    state = 'CS'
                elif c.lower() == 'm':
                    state = 'CS'
                elif c.lower() == 'n':
                    state = 'CS'
                elif c.lower() == 'o':
                    state = 'CS'
                elif c.lower() == 'p':
                    state = 'CS'
                elif c.lower() == 'q':
                    state = 'CS'
                elif c.lower() == 'r':
                    state = 'CS'
                elif c.lower() == 's':
                    state = 'CS'
                elif c.lower() == 't':
                    state = 'CS'
                elif c.lower() == 'u':
                    state = 'CS'
                elif c.lower() == 'v':
                    state = 'CS'
                elif c.lower() == 'w':
                    state = 'CS'
                elif c.lower() == 'x':
                    state = 'CS'
                elif c.lower() == 'y':
                    state = 'CS'
                elif c.lower() == 'z':
                    state = 'CS'
                elif c.lower() == '_':
                    state = 'CS'
                elif c.lower() == '<':
                    state = 'CS'
                elif c.lower() == '-':
                    state = 'CS'
                elif c.lower() == '+':
                    state = 'CS'
                elif c.lower() == '/':
                    state = 'CS'
                elif c.lower() == '*':
                    state = 'CS'
                elif c.lower() == '^':
                    state = 'CS'
                elif c.lower() == '>':
                    state = 'CS'
                elif c.lower() == '=':
                    state = 'CS'
                elif c.lower() == '.':
                    state = 'CS'
                elif c.lower() == ',':
                    state = 'CS'
                elif c.lower() == ';':
                    state = 'CS'
                elif c.lower() == ':':
                    state = 'CS'
                elif c.lower() == '(':
                    state = 'CS'
                elif c.lower() == ')':
                    state = 'CS'
                elif c.lower() == '[':
                    state = 'CS'
                elif c.lower() == ']':
                    state = 'CS'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'CS'
                elif c.lower() == '\t':
                    state = 'CS'
                elif c.lower() == ' ':
                    state = 'CS'
                elif c.lower() == '0':
                    state = 'CL'
                elif c.lower() == '1':
                    state = 'CL'
                elif c.lower() == '2':
                    state = 'CL'
                elif c.lower() == '3':
                    state = 'CL'
                elif c.lower() == '4':
                    state = 'CL'
                elif c.lower() == '5':
                    state = 'CL'
                elif c.lower() == '6':
                    state = 'CL'
                elif c.lower() == '7':
                    state = 'CL'
                elif c.lower() == '8':
                    state = 'CL'
                elif c.lower() == '9':
                    state = 'CL'
                elif c.lower() == '$':
                    state = 'CS'
                elif c.lower() == '\'':
                    state = 'CS'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'CS':
                tipo = 'numero'
                lerProxGlobal = False
                tabelaSimbolos[id[:-1].strip()] = Atributo(tipo, id[:-1].strip())
                return Token(tipo, id[:-1].strip(), linhaGlobal, colunaGlobal)
            case 'CM':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'CV'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'CT'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'CO':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'CU'
                elif c.lower() == '-':
                    state = 'CU'
                elif c.lower() == '+':
                    state = 'CU'
                elif c.lower() == '/':
                    state = 'CU'
                elif c.lower() == '*':
                    state = 'CU'
                elif c.lower() == '^':
                    state = 'CU'
                elif c.lower() == '>':
                    state = 'CU'
                elif c.lower() == '=':
                    state = 'CU'
                elif c.lower() == '.':
                    state = 'CU'
                elif c.lower() == ',':
                    state = 'CU'
                elif c.lower() == ';':
                    state = 'CU'
                elif c.lower() == ':':
                    state = 'CU'
                elif c.lower() == '(':
                    state = 'CU'
                elif c.lower() == ')':
                    state = 'CU'
                elif c.lower() == '[':
                    state = 'CU'
                elif c.lower() == ']':
                    state = 'CU'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'CU'
                elif c.lower() == '\t':
                    state = 'CU'
                elif c.lower() == ' ':
                    state = 'CU'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'CU'
                elif c.lower() == '\'':
                    state = 'CU'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'CU':
	            #Retorna Token 'inicio'
                tipo = 'inicio'
                lerProxGlobal = True
                f.seek(f.tell()-1)
                c = ''
                tabelaSimbolos[tipo] = Atributo(tipo, tipo)
                return Token(tipo, tipo, linhaGlobal, colunaGlobal)

            case 'CP':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'CV'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'CQ':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'CW'
                elif c.lower() == '-':
                    state = 'CW'
                elif c.lower() == '+':
                    state = 'CW'
                elif c.lower() == '/':
                    state = 'CW'
                elif c.lower() == '*':
                    state = 'CW'
                elif c.lower() == '^':
                    state = 'CW'
                elif c.lower() == '>':
                    state = 'CW'
                elif c.lower() == '=':
                    state = 'CW'
                elif c.lower() == '.':
                    state = 'CW'
                elif c.lower() == ',':
                    state = 'CW'
                elif c.lower() == ';':
                    state = 'CW'
                elif c.lower() == ':':
                    state = 'CW'
                elif c.lower() == '(':
                    state = 'CW'
                elif c.lower() == ')':
                    state = 'CW'
                elif c.lower() == '[':
                    state = 'CW'
                elif c.lower() == ']':
                    state = 'CW'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'CW'
                elif c.lower() == '\t':
                    state = 'CW'
                elif c.lower() == ' ':
                    state = 'CW'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'CW'
                elif c.lower() == '\'':
                    state = 'CW'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'CW':
                tipo = 'repita'
                lerProxGlobal = True
                f.seek(f.tell() - 1)
                c = ''
                tabelaSimbolos[id[:-1].strip()] = Atributo(tipo, id[:-1].strip())
                return Token(tipo, id[:-1].strip(), linhaGlobal, colunaGlobal)
            case 'CT':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'CX'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'CV':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'CY'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'AC'
                elif c.lower() == '-':
                    state = 'AC'
                elif c.lower() == '+':
                    state = 'AC'
                elif c.lower() == '/':
                    state = 'AC'
                elif c.lower() == '*':
                    state = 'AC'
                elif c.lower() == '^':
                    state = 'AC'
                elif c.lower() == '>':
                    state = 'AC'
                elif c.lower() == '=':
                    state = 'AC'
                elif c.lower() == '.':
                    state = 'AC'
                elif c.lower() == ',':
                    state = 'AC'
                elif c.lower() == ';':
                    state = 'AC'
                elif c.lower() == ':':
                    state = 'AC'
                elif c.lower() == '(':
                    state = 'AC'
                elif c.lower() == ')':
                    state = 'AC'
                elif c.lower() == '[':
                    state = 'AC'
                elif c.lower() == ']':
                    state = 'AC'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'AC'
                elif c.lower() == '\t':
                    state = 'AC'
                elif c.lower() == ' ':
                    state = 'AC'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'AC'
                elif c.lower() == '\'':
                    state = 'AC'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'CX':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'CZ'
                elif c.lower() == '-':
                    state = 'CZ'
                elif c.lower() == '+':
                    state = 'CZ'
                elif c.lower() == '/':
                    state = 'CZ'
                elif c.lower() == '*':
                    state = 'CZ'
                elif c.lower() == '^':
                    state = 'CZ'
                elif c.lower() == '>':
                    state = 'CZ'
                elif c.lower() == '=':
                    state = 'CZ'
                elif c.lower() == '.':
                    state = 'CZ'
                elif c.lower() == ',':
                    state = 'CZ'
                elif c.lower() == ';':
                    state = 'CZ'
                elif c.lower() == ':':
                    state = 'CZ'
                elif c.lower() == '(':
                    state = 'CZ'
                elif c.lower() == ')':
                    state = 'CZ'
                elif c.lower() == '[':
                    state = 'CZ'
                elif c.lower() == ']':
                    state = 'CZ'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'CZ'
                elif c.lower() == '\t':
                    state = 'CZ'
                elif c.lower() == ' ':
                    state = 'CZ'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'CZ'
                elif c.lower() == '\'':
                    state = 'CZ'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'CZ':
                tipo = 'enquanto'
                lerProxGlobal = True
                f.seek(f.tell() - 1)
                c = ''
                tabelaSimbolos[id[:-1].strip()] = Atributo(tipo, id[:-1].strip())
                return Token(tipo, id[:-1].strip(), linhaGlobal, colunaGlobal)
            case 'CY':
                c = nextChar()
                id += c
                colunaGlobal += 1
                if c.lower() == 'a':
                    state = 'C'
                elif c.lower() == 'b':
                    state = 'C'
                elif c.lower() == 'c':
                    state = 'C'
                elif c.lower() == 'd':
                    state = 'C'
                elif c.lower() == 'e':
                    state = 'C'
                elif c.lower() == 'f':
                    state = 'C'
                elif c.lower() == 'g':
                    state = 'C'
                elif c.lower() == 'h':
                    state = 'C'
                elif c.lower() == 'i':
                    state = 'C'
                elif c.lower() == 'j':
                    state = 'C'
                elif c.lower() == 'k':
                    state = 'C'
                elif c.lower() == 'l':
                    state = 'C'
                elif c.lower() == 'm':
                    state = 'C'
                elif c.lower() == 'n':
                    state = 'C'
                elif c.lower() == 'o':
                    state = 'C'
                elif c.lower() == 'p':
                    state = 'C'
                elif c.lower() == 'q':
                    state = 'C'
                elif c.lower() == 'r':
                    state = 'C'
                elif c.lower() == 's':
                    state = 'C'
                elif c.lower() == 't':
                    state = 'C'
                elif c.lower() == 'u':
                    state = 'C'
                elif c.lower() == 'v':
                    state = 'C'
                elif c.lower() == 'w':
                    state = 'C'
                elif c.lower() == 'x':
                    state = 'C'
                elif c.lower() == 'y':
                    state = 'C'
                elif c.lower() == 'z':
                    state = 'C'
                elif c.lower() == '_':
                    state = 'C'
                elif c.lower() == '<':
                    state = 'DA'
                elif c.lower() == '-':
                    state = 'DA'
                elif c.lower() == '+':
                    state = 'DA'
                elif c.lower() == '/':
                    state = 'DA'
                elif c.lower() == '*':
                    state = 'DA'
                elif c.lower() == '^':
                    state = 'DA'
                elif c.lower() == '>':
                    state = 'DA'
                elif c.lower() == '=':
                    state = 'DA'
                elif c.lower() == '.':
                    state = 'DA'
                elif c.lower() == ',':
                    state = 'DA'
                elif c.lower() == ';':
                    state = 'DA'
                elif c.lower() == ':':
                    state = 'DA'
                elif c.lower() == '(':
                    state = 'DA'
                elif c.lower() == ')':
                    state = 'DA'
                elif c.lower() == '[':
                    state = 'DA'
                elif c.lower() == ']':
                    state = 'DA'
                elif c.lower() == '\n':
                    linhaGlobal += 1
                    colunaGlobal = 0
                    state = 'DA'
                elif c.lower() == '\t':
                    state = 'DA'
                elif c.lower() == ' ':
                    state = 'DA'
                elif c.lower() == '0':
                    state = 'C'
                elif c.lower() == '1':
                    state = 'C'
                elif c.lower() == '2':
                    state = 'C'
                elif c.lower() == '3':
                    state = 'C'
                elif c.lower() == '4':
                    state = 'C'
                elif c.lower() == '5':
                    state = 'C'
                elif c.lower() == '6':
                    state = 'C'
                elif c.lower() == '7':
                    state = 'C'
                elif c.lower() == '8':
                    state = 'C'
                elif c.lower() == '9':
                    state = 'C'
                elif c.lower() == '$':
                    state = 'DA'
                elif c.lower() == '\'':
                    state = 'DA'
                else:
                    state = 'ER'
                    return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,colunaGlobal)
            case 'W':
                c = nextChar()
                if c == ']':
                    state = 'X'
                else:
                    state = 'W'
            case 'DA':
                tipo = 'programa'
                lerProxGlobal = True
                f.seek(f.tell()-1)
                c = ''
                tabelaSimbolos[id[:-1].strip()] = Atributo(tipo,id[:-1].strip())
                return Token(tipo,id[:-1].strip(),linhaGlobal,colunaGlobal)

'''def simuladorSintatico():
    global tabelaSimbolos
    while True:
        try:
            token = lex()
            print(f"<{token.tipo}, {token.atributo}, {token.linha}, {token.coluna}>")
            if token.tipo == 'Erro' or token.tipo == '$':
                break
        except EOFError:
            break
    print('Tabela de simbolos')
    for key, value in tabelaSimbolos.items():
        print(f"key {key} nome {value.nome} valor {value.valor}")
simuladorSintatico()'''