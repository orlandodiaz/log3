import logging

SUCCESS = 15


class Logger(logging.Logger):
    """ Subclassing the Logger class"""
    super(logging.Logger)

    def success(self, msg, *args, **kwargs):
        if self.isEnabledFor(SUCCESS):
            self._log(SUCCESS, msg, args, **kwargs)

    def disable_logging(self):
        self.setLevel(logging.WARNING)

    def enable_logging(self):
        self.setLevel(logging.DEBUG)

