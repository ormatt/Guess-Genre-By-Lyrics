from logger import logger


def load(path):
    try:
        with open(path, 'r') as reader:
            logger.info("Loading text from file %s" % path)
            return reader.read()
    except IOError as ex:
        logger.error("Could not load text from file %s - %s" % (path, ex))
        return ''
