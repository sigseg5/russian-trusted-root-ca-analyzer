import logging
import sys
from datetime import datetime


class RemoveNewlineFormatter(logging.Formatter):
    def format(self, record):
        msg = super().format(record)
        if msg.rstrip() == '':
            return ""
        return msg.rstrip()


class StdoutToLogger:
    def __init__(self, logger):
        self.logger = logger

    def write(self, message):
        if message.rstrip() != "":
            self.logger.info(message.rstrip())

    def flush(self):
        pass


class StdoutToLogger:
    def __init__(self, logger):
        self.logger = logger

    def write(self, message):
        self.logger.info(message)

    def flush(self):
        pass


# create logger
logger = logging.getLogger('CA-LOGGER')
logger.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# create file handler and set level to INFO
filename = datetime.now().strftime(
    "%Y-%m-%d %H:%M:%S") + '_logfile.log'
file_handler = logging.FileHandler(f'logs/{filename}')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(RemoveNewlineFormatter(formatter._fmt))

# create console handler and set level to INFO
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(RemoveNewlineFormatter(formatter._fmt))

# add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)
sys.stdout = StdoutToLogger(logger)