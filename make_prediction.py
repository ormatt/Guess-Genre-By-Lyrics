from __future__ import print_function
import os

import constants
from utils import persistence

SELF_DIR = os.path.dirname(os.path.abspath(__file__))
LYRIC_PATH = os.path.join(constants.RESOURCES_DIR, 'sample_song.txt')

CLF_NAME = constants.CLF_FITTED_DUMP_NAME


def predict_genre(data, clf):
    print('Prediction: %s' % clf.predict([data]))


def load_lyric(path):
    with open(path, 'r') as reader:
        return reader.read()


if __name__ == '__main__':
    clf = persistence.load(CLF_NAME)
    lyric = load_lyric(LYRIC_PATH)
    predict_genre(lyric, clf)
