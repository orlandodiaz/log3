import logging
from colorama import Fore, Back, Style
from logging.handlers import RotatingFileHandler


logger = logging.getLogger(__name__)
root_logger = logging.getLogger('urllib3')
stderr = None

COLWIDTH = 10

def configure_logger():
    if not logger.handlers:

        # LOGGING FORMAT

        fmt = '[%(asctime)s %(filename){}s] %(levelname)-6s - %(message)7s'.format(COLWIDTH)
        date_fmt = '%Y-%m-%d %H:%M:%S'
        formatter = logging.Formatter(fmt, datefmt=date_fmt)

        # STDERR LOGGING
        global stderr
        stderr = logging.StreamHandler()
        stderr.setFormatter(formatter)

        logger.addHandler(stderr)
        logger.setLevel(logging.DEBUG)

        root_logger.addHandler(stderr)
        root_logger.setLevel(logging.DEBUG)


def warning(msg, *args, **kwargs):
        fmt='{}[%(asctime)s %(filename){}s] %(levelname)-7s - %(message)7s{}'\
            .format(Fore.YELLOW, COLWIDTH, Style.RESET_ALL)

        date_fmt = '%Y-%m-%d %H:%M:%S'
        formatter = logging.Formatter(fmt, datefmt=date_fmt)

        # STDERR LOGGING
        global stderr
        stderr.setFormatter(formatter)
        logger.warning(msg, *args, **kwargs)

        # RESET THE LOGGING
        fmt='[%(asctime)s %(filename)18s] %(levelname)-7s - %(message)7s'
        formatter2 = logging.Formatter(fmt, datefmt=date_fmt)

        # STDERR LOGGING
        stderr.setFormatter(formatter2)


def error(msg, *args, **kwargs):
    fmt = '{}[%(asctime)s %(filename){}s] %(levelname)-7s - %(message)7s{}'\
        .format(Fore.RED, COLWIDTH, Style.RESET_ALL)
    date_fmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(fmt, datefmt=date_fmt)

    # STDERR LOGGING
    global stderr
    stderr.setFormatter(formatter)
    logger.error(msg, *args, **kwargs)

    fmt = '[%(asctime)s %(filename)18s] %(levelname)-7s - %(message)7s'
    formatter2 = logging.Formatter(fmt, datefmt=date_fmt)

    stderr.setFormatter(formatter2)

def info(msg, *args, **kwargs):
    logger.info(msg, *args, **kwargs)

def debug(msg, *args, **kwargs):
    logger.debug(msg, *args, **kwargs)
        

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

    if logroot:
        root_logger.addHandler(file_handler)
        root_logger.setLevel(logging.DEBUG)


def enable_logging():
    """ Sets logging level to DEBUG"""
    logger.setLevel(logging.DEBUG)

def disable_logging():
    """ Sets logging level to WARNING"""
    logger.setLevel(logging.WARNING)
    root_logger.setLevel(logging.WARNING)

configure_logger()
