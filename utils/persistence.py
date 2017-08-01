import os
from sklearn.externals import joblib

from constants import DUMPS_DIR
from utils.logger import logger


def dump(filename, obj):
    with open(os.path.join(DUMPS_DIR, filename), 'wb') as writer:
        joblib.dump(obj, writer)
        logger.debug('Dumped obj with filename %s to disk' % filename)


def load(filename):
    with open(os.path.join(DUMPS_DIR, filename), 'rb') as reader:
        obj = joblib.load(reader)
        logger.debug('Loaded obj with filename %s from disk' % filename)
    return obj
