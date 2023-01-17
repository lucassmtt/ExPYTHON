# Faça um programa completo utilizando classes e métodos que:
# Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
# tipoCombustivel, valorLitro, quantidadeCombustivel
# Possua no mínimo esses métodos:
# abastece por valor - método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
# abastecer por litro – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
# alterar valor – altera o valor do litro do combustível.
# alterar combustivel – altera o tipo do combustível.
# alterar quantidade combustivel – altera a quantidade de combustível restante na bomba.
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.

class Bomba_Combustivel:
    def __init__(self, tipo_combustivel='comum', valor_por_litro=5, quantidade_tot_gasolina=1000):
        self.tipo_combustivel = tipo_combustivel
        self.tot_gasolina = quantidade_tot_gasolina
        self.valor_por_litro = valor_por_litro


    def mostrar_tot_gasolina_da_bomba(self):
        print(f'Ainda resta nesta bomba {self.tot_gasolina:.2f} litros.')


    def abastecer_Por_Valor(self, valor):
        quantidade_retirada = valor / self.valor_por_litro

        if self.tot_gasolina <= 150:
            print('A gasolina da bomba está acabando, avise o proprietário para enche-lá.')


        if quantidade_retirada > self.tot_gasolina:
            print('Impossível abastecer. Esta bomba encontra-se sem gasolina')

        else:
            print(f'{valor}R$ = {quantidade_retirada:.2f}L')
            self.tot_gasolina -= quantidade_retirada


    def abastecer_Por_Litro(self, valor_litros):
        valor_abastecimento = valor_litros * self.valor_por_litro

        if self.tot_gasolina <= 150:
            print('A gasolina da bomba está acabando, avise o proprietário para enche-lá.')

        if valor_litros > self.tot_gasolina:
            print('Impossível abastecer. Esta bomba encontra-se sem gasolina')

        else:
            print(f'{valor_abastecimento}R$ = {valor_litros:.2f}L')
            self.tot_gasolina -= valor_litros


    def alterar_Valor(self, novo_valor):
        self.valor_por_litro = novo_valor


    def alterar_Combustivel(self, novo_combustivel):
        self.tipo_combustivel = novo_combustivel


    def alterar_Quant_Combustivel(self, valor_adicionar_ou_tirar):
        self.tot_gasolina += valor_adicionar_ou_tirar




if __name__ == '__main__':
    bomba_lateral_esquerda = Bomba_Combustivel(tipo_combustivel='comum',
                                               valor_por_litro=4.50,
                                               quantidade_tot_gasolina=600)

    bomba_frontal = Bomba_Combustivel(tipo_combustivel='etanol',
                                      valor_por_litro=4.10,
                                      quantidade_tot_gasolina=800)

    bomba_lateral_esquerda.abastecer_Por_Valor(300)
    bomba_lateral_esquerda.mostrar_tot_gasolina_da_bomba()
    bomba_lateral_esquerda.abastecer_Por_Litro(100)
    bomba_lateral_esquerda.abastecer_Por_Litro(100)
    bomba_lateral_esquerda.abastecer_Por_Litro(100)
    bomba_lateral_esquerda.abastecer_Por_Litro(100)
    bomba_lateral_esquerda.mostrar_tot_gasolina_da_bomba()
    bomba_lateral_esquerda.abastecer_Por_Valor(400)
    bomba_lateral_esquerda.mostrar_tot_gasolina_da_bomba()
    bomba_lateral_esquerda.abastecer_Por_Litro(50)

    bomba_lateral_esquerda.alterar_Combustivel('comum')
    bomba_lateral_esquerda.alterar_Valor(5)
    bomba_lateral_esquerda.alterar_Quant_Combustivel(100)
    bomba_lateral_esquerda.abastecer_Por_Litro(50)
    bomba_lateral_esquerda.alterar_Quant_Combustivel(-100)
    bomba_lateral_esquerda.mostrar_tot_gasolina_da_bomba()
