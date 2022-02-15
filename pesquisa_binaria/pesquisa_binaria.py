def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    
    print('primeiro alto: ' + str(alto)) 

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        print('meio: ' + str(meio) + ' chute: ' + str(chute) + ' baixo: ' + str(baixo) + ' alto: ' + str(alto)) 
 
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
            
    return None

minha_lista = [1, 3, 5, 7, 9, 19, 40, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 50000]

print(pesquisa_binaria(minha_lista, 7))
print(pesquisa_binaria(minha_lista, -1))