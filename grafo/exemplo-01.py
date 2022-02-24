from collections import deque

grafo = {}
grafo["voce"] = ["alice", "bob", "claire"]
grafo["bob"] = ["anuj", "peggy"]
grafo["alice"] = ["peggy"]
grafo["claire"] = ["thom", "jony", "mike"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["thom"] = []
grafo["jony"] = []

fila_de_pesquisa = deque()
fila_de_pesquisa += grafo["voce"]

def pessoa_e_vendedora(nome):
    return nome[-1] == 'm'

def pesqusia(nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[nome]
    verificadas = []
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if not pessoa in verificadas:
            if pessoa_e_vendedora(pessoa):
                print(pessoa)
                return True
            else:
                fila_de_pesquisa += grafo[pessoa]
                verificadas.append(pessoa)
    return False

print(pesqusia("claire"))