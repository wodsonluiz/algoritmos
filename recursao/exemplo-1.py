def procure_pela_chave(caixa_principal):
    pilha = main_box.crie_uma_pilha_busca()
    while pilha is not vazia:
        caixa = pilha.peque_caixa()
        for item in caixa:
            if item.e_uma_caixa():
                pilha.append(item)
            elif item.e_uma_chave():
                print("achei a chave!")