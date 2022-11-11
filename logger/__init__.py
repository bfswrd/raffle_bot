import logging

file_log = logging.FileHandler('info.log')
console_out = logging.StreamHandler()

format_log = ('%(asctime)s | '
              '%(levelname)s | %(name)s:'
              '%(funcName)s:%(lineno)d - '
              '%(message)s')

logging.basicConfig(
    handlers=[file_log, console_out],
    level=logging.INFO,
    format=format_log,
    datefmt='%d-%m-%Y %H:%M:%S'
)

logger = logging
