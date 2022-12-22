class Log:
    def log(self, msg):
        raise NotImplementedError('Implemente o metodo log')

class LogFileMixin(Log):
    def log(self, msg):
        print(self.__class__.__name__)

class Log