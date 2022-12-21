# class Carro:
#     def __init__(self, nome_do_carro):
#         self.nome_do_carro = nome_do_carro
#         self.nome_do_motor = None
#         self.info_carro = []
#
#     def add_motor(self, nome_do_motor):
#         self.info_carro.append(Motor(nome_do_motor, self.nome_do_carro))
#
#     def listar(self):
#         for carro in self.info_carro:
#             print(carro.nome_do_carro, carro.nome_do_motor)
#
#
# class Motor:
#     def __init__(self, nome_do_motor, nome_do_carro):
#         self.nome_do_motor = nome_do_motor
#         self.nome_do_carro = nome_do_carro
#
# class Fabricante:
#     def __init__(self, carro_a_fabricar):
#         self.carro = carro_a_fabricar
#
#
#
#
# carro_do_motta = Carro('Fusca')
# carro_do_motta.add_motor('V8')

class Carro:
    def __init__(self, nome_do_carro):
        self.nome = nome_do_carro
        self._motor = None
        self._fabricante = None
    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome_do_motor):
        self.nome_do_motor = nome_do_motor

class Fabricante:
    def __init__(self, nome_da_fabricante):
        self.nome_da_fabricante = nome_da_fabricante


Fusca = Carro('Fusca')
motor_1_0 = Motor('1.0')
Volksvagen = Fabricante('Volksvagen')

Fusca.motor = motor_1_0
Fusca.fabricante = Volksvagen
Fusca.motor = motor_1_0

print(Fusca.nome, Fusca.fabricante.nome_da_fabricante, Fusca.motor.nome_do_motor)