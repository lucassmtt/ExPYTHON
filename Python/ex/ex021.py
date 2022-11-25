produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dc = {
    chave: valor
    if isinstance(valor, (int, float)) else valor
    for chave, valor
    in produto.items()

}

print(dc)