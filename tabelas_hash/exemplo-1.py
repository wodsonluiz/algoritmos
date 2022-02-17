def CriarTabelaHash(nome):
    lista_telefone = {}
    lista_telefone["wodson"] = "9999-9999"
    lista_telefone["wagner"] = "8888-8888"
    lista_telefone["wesley"] = "7777-7777"

    return lista_telefone[nome]

print(CriarTabelaHash("wagner"))

