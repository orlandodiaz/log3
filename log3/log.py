import logging
from .my_logger import Logger
from .my_formatter import MyFormatter
from logging.handlers import RotatingFileHandler

logger = Logger(__name__)
urllib_logger = logging.getLogger('urllib3')


def config():
    global logger
    global urllib_logger

    fmt = MyFormatter()

    logging.addLevelName(15, 'SUCCESS')

    # STDERR LOGGING
    stderr = logging.StreamHandler()
    # fmt = '[%(asctime)s %(filename)18s] %(levelname)-7s - %(message)7s'
    date_fmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(fmt, datefmt=date_fmt)
    stderr.setFormatter(fmt)
    logger.addHandler(stderr)
    logger.setLevel(logging.WARNING)

    urllib_logger.addHandler(stderr)
    urllib_logger.setLevel(logging.WARNING)


config()


def log_to_file(log_path, log_urllib=False, limit=None):
    """ Add file_handler to logger"""
    log_path = log_path
    file_handler = logging.FileHandler(log_path)
    if limit:
        file_handler = RotatingFileHandler(
            log_path,
            mode='a',
            maxBytes=limit * 1024 * 1024,
            backupCount=2,
            encoding=None,
            delay=0)
    fmt = '[%(asctime)s %(filename)18s] %(levelname)-7s - %(message)7s'
    date_fmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(fmt, datefmt=date_fmt)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    if log_urllib:
        urllib_logger.addHandler(file_handler)
        urllib_logger.setLevel(logging.DEBUG)
