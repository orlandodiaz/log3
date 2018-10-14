import logging
from colorama import Fore, Back, Style
from logging.handlers import RotatingFileHandler
import inspect
import os

# logger = logging.getLogger(__name__)
root_logger = logging.getLogger('urllib3')
logger = None
stderr = None
COLWIDTH = 10

_fmt = '{color}[%(asctime)s {filename:>{colwidth}}] %(levelname)-7s - %(message)7s{end}'


def config(name):
        # if not logger.handlers:

        global logger
        logger = logging.getLogger(name)

        # STDERR LOGGING
        global stderr
        stderr = logging.StreamHandler()
        # stderr.setFormatter(formatter)

        logger.addHandler(stderr)
        logger.setLevel(logging.DEBUG)

        root_logger.addHandler(stderr)
        root_logger.setLevel(logging.DEBUG)

        log_path = 'myloggingfile'
        limit=None
        file_handler = logging.FileHandler(log_path)
        if limit:
            file_handler = RotatingFileHandler(log_path, mode='a', maxBytes=limit * 1024 * 1024,
                                               backupCount=2, encoding=None, delay=0)

        fmt = '[%(asctime)s %(filename)18s] %(levelname)-7s - %(message)7s'
        date_fmt = '%Y-%m-%d %H:%M:%S'
        formatter = logging.Formatter(fmt, datefmt=date_fmt)

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)


def _get_filename():
    """ Get the calling module's filename"""

    previous_frame = inspect.currentframe().f_back.f_back
    (filename, line_number,
     function_name, lines, index) = inspect.getframeinfo(previous_frame)

    # log calls not enclosed in a function will return filename  instead of just input
    if filename == '<input>':
            filename =  previous_frame.f_locals['__file__']

    filename = os.path.basename(filename)

    return filename


def warning(msg, *args, **kwargs):
    """ Log a warning """

    fmt=_fmt.format(color=Fore.YELLOW, colwidth=COLWIDTH, filename=_get_filename(), end=Style.RESET_ALL)

    date_fmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(fmt, datefmt=date_fmt)

    # STDERR LOGGING
    global stderr
    stderr.setFormatter(formatter)
    logger.warning(msg, *args, **kwargs)


def boilerplate(fmt):
    """ Boilerplate for the logging methods

    This boilerplate code has common code logic

    Args:
        fmt: The formatter object

    """

    date_fmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(fmt, datefmt=date_fmt)

    # STDERR LOGGING
    global stderr
    stderr.setFormatter(formatter)


def error(msg, *args, **kwargs):
    """ Log an error message"""

    fmt = _fmt.format(color=Fore.RED, colwidth=COLWIDTH, filename=_get_filename(), end=Style.RESET_ALL)

    boilerplate(fmt)
    logger.error(msg, *args, **kwargs)


def info(msg, *args, **kwargs):

    fmt = _fmt.format(color=Fore.BLUE, colwidth=COLWIDTH, filename=_get_filename(), end=Style.RESET_ALL)

    boilerplate(fmt)
    logger.info(msg, *args, **kwargs)


def debug(msg, *args, **kwargs):
    fmt = _fmt.format(color=Fore.LIGHTBLACK_EX, colwidth=COLWIDTH, filename=_get_filename(), end=Style.RESET_ALL)

    boilerplate(fmt)
    logger.debug(msg, *args, **kwargs)


def success(msg, *args, **kwargs):
    """ Custom log method meant to be used for successful operations"""

    logging.addLevelName(15, 'SUCCESS')

    fmt = _fmt.format(color=Fore.GREEN, colwidth=COLWIDTH, filename=_get_filename(), end=Style.RESET_ALL)

    boilerplate(fmt)
    if logger.isEnabledFor(15):
        logger._log(15, msg, args, **kwargs)


def log_to_file(log_path, logroot=True, limit=None):
    """ Adds filename handler to the logger


    Args:
        log_path: Path to logfile
        logroot:  True to log root handler
        limit:    Limit the size of the log file. New log will be created if size is exceeded

    """

    file_handler = logging.FileHandler(log_path)
    if limit:
        file_handler = RotatingFileHandler(log_path, mode='a', maxBytes=limit * 1024 * 1024,
                                         backupCount=2, encoding=None, delay=0)

    fmt = '[%(asctime)s %(filename)18s] %(levelname)-7s - %(message)7s'
    date_fmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(fmt, datefmt=date_fmt)

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    #
    # if logroot:
    #     root_logger.addHandler(file_handler)
    #     root_logger.setLevel(logging.DEBUG)


def enable_logging():
    """ Sets logging level to the lowest (DEBUG) """

    logger.setLevel(logging.DEBUG)


def disable_logging():
    """ Sets logging level to the highest (WARNING) """

    logger.setLevel(logging.WARNING)
    root_logger.setLevel(logging.WARNING)


# _configure_logger()
