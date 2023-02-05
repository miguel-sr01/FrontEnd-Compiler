'''
Analisador Sintatico
Alunos: Douglas Gomes de Paula - Matricula: 11621BCC013
        Miguel Sanches Rocha - Matricula: 11811BCC001
'''

import pandas as pd
import numpy as np

import lexico

#************************** TABELA DE ANALISE PREDITIVA E VETOR DE PRODUÇÕES ************************************

#Tabela de Análise Preditiva
df1 = pd.read_excel('tabelaPreditivaExcel.xlsx')
tabela_preditiva = np.asarray(df1)

#Vetor de Producoes
df2 = pd.read_excel('vetorProducoes.xlsx')
vetor_producoes = np.asarray(df2)

#Numero de Linhas e Colunas da Tabela de Análise Preditiva
numero_linhasTab = df1.shape[0]
numero_colunasTab = df1.shape[1]

#Numero de Linhas e Colunas do Vetor de Producoes
numero_linhasVet = df2.shape[0]
numero_colunasVet = df2.shape[1]


#************************** FUNÇÕES AUXILIARES ************************************

#Função para pegar a tupla(linhas,coluna) de determinado simbolo. Ex: pegaLinhaColunaNaoTerminal("S")
def pega_linha_coluna(simbolo):
    for i in range(0,numero_linhasTab):
        for j in range(0,numero_colunasTab):
            if tabela_preditiva[i][j] == simbolo:
                return i,j
    return None

#Função que retorna valores da tabela, dado um Não Terminal e um Terminal. Ex: pegaValorTabela("declaracao_das_variaveis","identificador")
def pegaValorTabela(NTerminal, Terminal):
    #print('Nterminal', NTerminal)
    #print('terminal', Terminal)
    linhaNTerminal, colunaNTerminal = pega_linha_coluna(NTerminal)
    linhaTerminal, colunaTerminal = pega_linha_coluna(Terminal)

    return tabela_preditiva[linhaNTerminal][colunaTerminal]

#Função que retorna a producao correta, dado um Não Terminal e um Terminal. Ex: pega_vetor_producoes("S","programa")
def pega_vetor_producoes(NTerminal, Terminal):
    linhaNTerminal, colunaNTerminal = pega_linha_coluna(NTerminal)
    linhaTerminal, colunaTerminal = pega_linha_coluna(Terminal)
    valor = tabela_preditiva[linhaNTerminal][colunaTerminal]
    producao = vetor_producoes[valor-1][1]

    return producao.split()




#******************************************* PILHA ****************************************************

class Nodo:

    def __init__(self, dado=None, nodo_anterior=None):
        self.dado = dado
        self.anterior = nodo_anterior

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.anterior)


class Pilha:

    def __init__(self):
        self.topo = None
        self.lista = []
        self.lista2 = []
        self.tamanho = 0

    def __repr__(self):
        return "[" + str(self.topo) + "]"

    def push(self, novo_dado):

        # Cria um novo nodo com o dado a ser armazenado.
        novo_nodo = Nodo(novo_dado)

        self.lista.append(novo_dado)

        # Faz com que o novo nodo seja o topo da pilha.
        novo_nodo.anterior = self.topo

        # Faz com que a cabeça da lista referencie o novo nodo.
        self.topo = novo_nodo

        # Adiciona 1 no tamanho da pilha
        self.tamanho = self.tamanho + 1

    def pop(self):

        assert self.topo, "Impossível remover valor de pilha vazia."

        self.topo = self.topo.anterior

        self.tamanho = self.tamanho - 1

        self.lista.pop()

    def pilha_vazia(self):
        if self.topo == None:
            return True
        else:
            return False

    def pega_topo(self):
        if self.pilha_vazia():
            return None
        else:
            return self.lista[len(self.lista)-1]


#******************************************* ARVORE ****************************************************
class Arvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita
        self.lista = []


    def pega_subarvore(self):
        return '%s\n %s' % (self.chave, self.lista)

def estrutura_floresta(floresta):
    for j in range(0, len(floresta)):
        print(floresta[j])




#********************************** ALGORITMO ANALISE PREDITIVA *******************************************
def algoritmo_analise_preditiva():
    #Lista de terminais
    terminal = ["programa", "identificador", "inicio", "fim", "tipo", ";", ":", "se", "(", ")", "entao", "senao", "enquanto", "faca", "repita", "<--", "op_rela", "+", "-", "*", "/", "^", "numero", "letra", ",", "$"]

    #Inicializa Floresta, Pilha, empilha simbolo inicial "S"
    floresta = []
    pilha = Pilha()
    pilha.push("S")

    #Chama proximo token pro lexico
    token = lexico.lex()
    #Atribui token.tipo à variavel proxToken
    proxToken = token.tipo

    #Enquanto pilha não for vazia
    while pilha.pilha_vazia() == False:
        x = pilha.pega_topo()
        if x in terminal:
            if x == proxToken:
                pilha.pop()
                token = lexico.lex()
                proxToken = token.tipo
            else:
                print(f"ERRO! TOKEN \"{token.atributo}\" NÃO ERA ESPERADO!\nErro presente na Linha: {token.linha} Coluna: {token.coluna} ".format(token.atributo))
                exit()
        else:
            valor = pegaValorTabela(x, proxToken)
            if valor == -1:
                print(f"ERRO! TOKEN \"{token.atributo}\" NÃO ERA ESPERADO!\nErro presente na Linha: {token.linha} Coluna: {token.coluna} ".format(token.atributo))
                exit()
            else:
                #Trata Produção : Construi a sub_arvore
                sub_arvore = Arvore(x)

                #Pega vetor de producao correspondente
                producao = pega_vetor_producoes(x, proxToken)

                #Adiciona retorno da produção à lista da sub_arvore
                for k in range(0, len(producao)):
                    sub_arvore.lista.append(producao[k])

                # Adiciona arvore à floresta
                floresta.append(sub_arvore.pega_subarvore())

                #Retira o topo da pilha
                pilha.pop()
                #Pega vetor de producao correspondente
                producao = pega_vetor_producoes(x, proxToken)
                #Empilha todos os simbolos na ordem inversa
                if producao[0] != 'ε':
                    for i in range (0, len(producao)):
                        pilha.push(producao[i])

    #Ao sair do while, se o proxToken não for "$", erro!
    if proxToken != "$":
        print(f"ERRO! TOKEN \"{token.atributo}\" NÃO ERA ESPERADO!\nErro presente na Linha: {token.linha} Coluna: {token.coluna} ".format(token.atributo))
        exit()

    #Se o proxToken for "$", sucesso!
    else:
        print("SUCESSO! SEU PROGRAMA FOI ACEITO PELO ANALISADOR SINTÁTICO!")

        #Retorna Floresta construida
        return floresta







if __name__ == '__main__':
    floresta = algoritmo_analise_preditiva()
    estrutura_floresta(floresta)









