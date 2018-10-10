import pytest

import os

@pytest.fixture
def log():
    from log3 import log
    return log

def test_log_info(capsys):
    from log3 import log

    log.info("info")
    _, stderr = capsys.readouterr()

def test_log_error(capsys):
    from log3 import log

    log.error("error")
    _, stderr = capsys.readouterr()

def test_log_debug(capsys):
    from log3 import log

    log.debug("debug")
    _, stderr = capsys.readouterr()

    assert "debug" in stderr
def test_log_warning(capsys):
    from log3 import log

    log.warning("warning")
    _, stderr = capsys.readouterr()

    assert "warning" in stderr

def test_enable_logging(log):
    log.enable_logging()
    assert log.logger.level == 10

def test_disable_logging(log):
    log.disable_logging()
    assert log.logger.level == 30

def test_file_logging(log):
    # from log3 import log

    log.log_to_file('/tmp/mylog')
    log.enable_logging()
    log.info('logged to file')

    file = open('/tmp/mylog', 'r+')
    try:
        line1 = file.readline()
        # os.system('say hi {}'.format(line1))
        assert 'logged to file' in line1
    finally:
        file.close()
        os.remove('/tmp/mylog')


