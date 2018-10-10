# Log3

`Log3` is a module that makes it easier to log to python. `Log3` comes with
 a strong default logging configuration system so that you don't configure them
 yourself.

 Also if you're working with console. log will display a colored output

 ## Installation

    pip install log3

## Usage

 To start logging it is as simple as importing the log and issuing the logging
 commands:

    from log3 import log

    log.info("Hello world")
    log.debug("This is a debug message")
    log.warning("This is a warning")
    log.error("This is an error")

#### Log to file

    log.log_to_file('file')
    log.info('logged to file')

### Disable logging

You can quickly disable logging rather than hardcoding it into your logging
configuration file

    log.disable_logging()

To start logging again is also that simple:

    log.enable_logging()

What it's really doing is changing the logger levels from DEBUG to WARNING
which


