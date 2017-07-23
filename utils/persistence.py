import os
from constants import DUMPS_DIR
from utils.logger import logger

try:
    import cPickle as pickle
except ImportError:
    import pickle


def dump(filename, obj):
    with open(os.path.join(DUMPS_DIR, filename + '.pickle'), 'wb') as writer:
        pickle.dump(obj, writer)
        logger.debug('Dumped obj with filename %s to disk' % filename)


def load(filename):
    with open(os.path.join(DUMPS_DIR, filename + '.pickle'), 'rb') as reader:
        obj = pickle.load(reader)
        logger.debug('Loaded obj with filename %s from disk' % filename)
    return obj
