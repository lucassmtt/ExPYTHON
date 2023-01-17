class Carro:
    def __init__(self, consumo_por_km):
        self.tanque = 5 #está na reserva
        self.consumo_por_km = consumo_por_km

    def pode_andar_quantos_km_ainda(self):
        qts_km = self.consumo_por_km * self.tanque
        return int(qts_km)

    def andar(self, valor_em_km):
        if valor_em_km > self.pode_andar_quantos_km_ainda():
            print('Impossível andar essa distância, a gasolina acabará.')
        else:
            qtd_gasolina_gastada = valor_em_km / self.consumo_por_km
            self.tanque -= qtd_gasolina_gastada

    def obter_gasolina(self):
        print(f'Quantidade de gasolina restante {self.tanque}, isso se traduz em mais ou menos'
              f' {self.pode_andar_quantos_km_ainda()}KM.')
        if self.tanque <= 5:
            print('O carro está na reserva...')

fusca = Carro(10)
fusca.andar(30)
fusca.obter_gasolina()
fusca.andar(10)