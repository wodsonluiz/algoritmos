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

def pessoa_e_vendedor(pessoa):
    return pessoa[-1] == 'm'

while fila_de_pesquisa:
    pessoa = fila_de_pesquisa.popleft()
    if pessoa_e_vendedor(pessoa):
        print("vender de manga", pessoa)
        break
    else:
        print("nao e vendedor")
        fila_de_pesquisa += grafo[pessoa]