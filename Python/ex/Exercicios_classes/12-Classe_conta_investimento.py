class ContaInvestimento:
    def __init__(self, numero_conta=0, nome_cliente='', saldo_inical=0, taxa_juros=0):
        self.numero = numero_conta
        self.nome = nome_cliente
        self.saldo = saldo_inical
        self.taxa = taxa_juros

    def add_juros(self, porc_juros):
        self.taxa = porc_juros

    
