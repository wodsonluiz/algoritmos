cache = {}
cache["http://www.google.com"] = "Google"

def paga_pagina(url):
    if cache.get(url):
        print("Pagina encontrada no cache")
        return cache[url]
    else:
        print("Pagina nao encontrada no cache")
        dados = pega_dados_servidor(url)
        cache[url] = dados
        return dados

def pega_dados_servidor(url):
    return url

print(paga_pagina("http://www.google.com"))