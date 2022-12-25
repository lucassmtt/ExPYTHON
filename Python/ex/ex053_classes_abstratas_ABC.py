from abc import ABC, abstractmethod

class Log(ABC):
    @abstractmethod # <-- classe Abstrata
    def _log(self, msg):
        ...

    def log_error(self, msg):
        print(f'ERROR {msg}')

    def log_success(self, msg):
        print(f'SUCCESS {msg}')

class LogPrintMixin(Log):
    def _log(self, msg):
        print(self.__class__.__name__, (msg))

log_01 = LogPrintMixin()
log_01.log_error('Olá mundo')

# class AbstractFoo(ABC):
#     def __init__(self):
#         ...

# class ConcretFoo(AbstractFoo):
#
