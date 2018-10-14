import logging
from colorama import Fore, Back, Style


class MyFormatter(logging.Formatter):
    _fmt = '{color}[%(asctime)s %(filename)18s] %(levelname)-7s - %(message)7s{end}'

    err_fmt = _fmt.format(color=Fore.RED, colwidth=10, end=Style.RESET_ALL)
    info_fmt = _fmt.format(color=Fore.BLUE, colwidth=10, end=Style.RESET_ALL)
    dbg_fmt = _fmt.format(color=Fore.LIGHTBLACK_EX, colwidth=10, end=Style.RESET_ALL)
    warning_fmt = _fmt.format(color=Fore.YELLOW, colwidth=10, end=Style.RESET_ALL)
    success_fmt = _fmt.format(color=Fore.LIGHTGREEN_EX, colwidth=10, end=Style.RESET_ALL)
    critical_fmt = _fmt.format(color=Fore.LIGHTRED_EX, colwidth=10, end=Style.RESET_ALL)

    def __init__(self):
        super().__init__(fmt="%(levelno)d: %(msg)s", datefmt=None, style='%')

    def format(self, record):

        # Save the original format configured by the user
        # when the logger formatter was instantiated
        format_orig = self._style._fmt

        # Replace the original format with one customized by logging level
        if record.levelno == logging.DEBUG:
            self._style._fmt = MyFormatter.dbg_fmt

        elif record.levelno == logging.INFO:
            self._style._fmt = MyFormatter.info_fmt

        elif record.levelno == logging.ERROR:
            self._style._fmt = MyFormatter.err_fmt
        elif record.levelno == logging.WARNING:
            self._style._fmt = MyFormatter.warning_fmt

        elif record.levelno == 15:
            self._style._fmt = MyFormatter.success_fmt

        elif record.levelno == logging.CRITICAL:
            self._style._fmt = MyFormatter.critical_fmt

        # Call the original formatter class to do the grunt work
        result = logging.Formatter.format(self, record)

        # Restore the original format configured by the user
        self._style._fmt = format_orig

        return result

