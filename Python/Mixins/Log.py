class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método em outra classe para usá-lo')

    def log_error(self, msg):
        return self._log(f'ERROR {msg}')

class LogFileMixin(Log):
    def _log(self, msg):
        print(msg)


class LogPrintMixin(Log):
    def _log(self, msg):
        print()


if __name__ == '__main__':
    l = LogFileMixin()
