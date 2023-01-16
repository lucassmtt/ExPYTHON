# Faça um programa que simule um televisor criando-o como um objeto.
# O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
# Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.

import json
class Televisao:
    def __init__(self):
        self.volume_atual = 30
        try:
            with open('tv.json', 'r') as arquivo:
                canal = json.load(arquivo)
                print(f'Canal atual: {canal}')
                self.canal_atual = canal
        except:
            self.canal_atual = input('Digite o canal que você gostaria de assistir:')
            with open('tv.json', 'w+') as arquivo:
                arquivo.write(self.canal_atual)



    def mudar_canal(self, novo_canal):
        self.canal_atual = novo_canal
        print(f'Canal atual: {novo_canal}')

    def mudar_volume(self, valor_aumentar_ou_diminuir=1):
        if self.volume_atual < 100 and self.volume_atual > 0:
            valor_final_apos_aumento = self.volume_atual + valor_aumentar_ou_diminuir
            if valor_final_apos_aumento < 100 and valor_final_apos_aumento > 0:
                self.volume_atual += valor_aumentar_ou_diminuir
            else:
                print('Esse valor excede o valor máximo para diminuir ou aumentar')

tv = Televisao()

# print(tv.volume_atual)
# tv.mudar_volume(40)
# print(tv.volume_atual)
# tv.mudar_volume(-10)
# print(tv.volume_atual)
# tv.mudar_volume(45)
print(tv.volume_atual)
tv.mudar_volume()
tv.mudar_volume()
tv.mudar_volume()
tv.mudar_volume()
tv.mudar_volume()
tv.mudar_volume()
tv.mudar_volume()
print(tv.volume_atual)