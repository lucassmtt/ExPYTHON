class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum([
            p.preco for p in self._produtos
        ])

    def add_produtos(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto)
    def listar_valor_produtos(self):
        for produto in self._produtos:
            print()
            print(produto.preco)


class Produto:
    def __init__(self, nome_produto, preco_produto):
        self.produto = nome_produto
        self.preco = preco_produto


carrinho = Carrinho()
p1, p2, p3 = Produto('Caneta',2), Produto('Camiseta', 50), Produto('Carregador', 20)
carrinho.add_produtos(p1, p2, p3)
carrinho.listar_valor_produtos()
print()
carrinho.total()
