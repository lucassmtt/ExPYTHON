produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

produto_maiusculo = {
    chave: valor.upper()
    if isinstance(valor, (int, str)) else valor
    for chave, valor
    in produto.items()

}


produto_so_categoria = {
    k: v
    for k, v in produto.items()
    if k == 'categoria'
}

produto_apenas_nome = {
    k: v
    for k, v in produto.items()
    if k == 'nome'
}

produto_trocado = {
    c: v
    for c, v in produto.items()
    if v != 'Caneta Azul'
}

apenas_caneta_azul = {
    k: v
    for k, v in produto.items()
    if v == 'Caneta Azul' or v == 2.5
}
print('Produto com .upper',produto_maiusculo)
print('Produto apenas "categoria"', produto_so_categoria)
print('Produto apenas "nome"', produto_apenas_nome)
print('Produto excluido, "caneta azul"', produto_trocado)
print('Apenas o produto "Caneta Azul" com o seu preço', apenas_caneta_azul)