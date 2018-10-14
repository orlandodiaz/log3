import logging

logger = logging.getLogger(__name__)
root_logger = logging.getLogger('urllib3')

def config():
    global logger
    global root_logger

    # STDERR LOGGING
    stderr = logging.StreamHandler()
    fmt = '[%(asctime)s %(filename)18s] %(levelname)-7s - %(message)7s'
    date_fmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(fmt, datefmt=date_fmt)
    stderr.setFormatter(formatter)
    logger.addHandler(stderr)
    logger.setLevel(logging.DEBUG)

    root_logger.addHandler(stderr)
    root_logger.setLevel(logging.DEBUG)


    ########## LOG TO FILE ################
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
    print('this got printed')
config()
