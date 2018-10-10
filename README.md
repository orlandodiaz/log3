# Log3

[![codecov](https://codecov.io/gh/orlandodiaz/log3/branch/master/graph/badge.svg)](https://codecov.io/gh/orlandodiaz/log3)
[![Build Status](https://travis-ci.com/orlandodiaz/log3.svg?branch=master)](https://travis-ci.com/orlandodiaz/log3)
![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)

`Log3` makes it easier to log to python. `Log3` comes with a strong default
logging configuration system so you don't configure them yourself.

If you're working with the console a lot, log will display a colored output.

 ## Installation

    pip install log3

## Usage

 To start logging it is as simple as importing the `log` object and issuing the logging
 commands:

    from log3 import log

    log.info("Hello world")
    log.debug("This is a debug message")
    log.warning("This is a warning")
    log.error("This is an error")

#### Log to file

    log.log_to_file('file')
    log.info('logged to file')

#### Disable logging

You can quickly disable logging rather than hardcoding it into your logging
configuration file.

    log.disable_logging()

To enable logging again it is also that simple:

    log.enable_logging()


