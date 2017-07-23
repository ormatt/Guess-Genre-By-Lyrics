import logging

LOGLEVEL = 'DEBUG'

logging.basicConfig(level=LOGLEVEL,
                    format='[%(asctime)s] - '
                           '[%(levelname)s] - '
                           '[%(module)s %(funcName)s] - '
                           '%(message)s')
logger = logging.getLogger("guess_logger")
