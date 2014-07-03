import logging
from wikiautils.logger import Logger

log = Logger(__name__)
log.setLevel(logging.DEBUG)
log.info('info')
