from pathlib import Path
import json

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método em outra classe para usá-lo')

    def error(self, msg):
        return self._log(f'ERROR')

    def success(self, msg):
        return self._log(f'SUCCESS')

class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        with open(LOG_FILE, 'a+', encoding='UTF8') as arquivo:
            arquivo.write(msg)
            arquivo.write('\n')
class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg}, ({self.__class__.__name__})')


if __name__ == '__main__':
    log_print = LogPrintMixin()
    log_print.error('Olá')
    log_print.success('Mundo')
    print()

    log_file = LogFileMixin()
    log_file.error('Meu nome')
    log_file.success('é Lucas')