from abc import ABC, abstractmethod

class Notifcacao(ABC):
    def __init__(self, msg) -> None: #usamos isso para identificação do desenvolvedor
        self.msg = msg

    @abstractmethod
    def enviar(self) -> bool:
        ...


class NotificacaoEmail(Notifcacao):
    def enviar(self) -> bool:
        print(f'E-mail - {self.msg}')
        return True


class NotificacaoSms(Notifcacao):
    def enviar(self) -> bool:
        print(f'SMS - {self.msg}')
        return True


def notificar(notificacao: Notifcacao):
    not_enviada = notificacao.enviar()
    if not_enviada:
        print('Notificação enviada com sucesso!')
    else:
        print('Erro ao enviar a notificação!')

notificar(NotificacaoSms('Ola')) #aqui se aplica o polimorfismo, onde a função funciona tanto com a
                                 #"NotificacaoSMS quanto com a do Email === polimorfismo