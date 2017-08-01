from __future__ import print_function
import os
import logging

import constants
from utils import dynamic_loading, persistence, text_from_file
from utils.logger import logger

try:
    from drafts import dev_fetch_lyrics as fetch_lyrics
except ImportError:
    fetch_lyrics = None

SELF_DIR = os.path.dirname(os.path.abspath(__file__))
CLF_NAME = constants.CLF_FITTED_DUMP_NAME

# Python 3 input is similar to Python 2 raw_input
try:
    input = raw_input
except NameError:
    pass


def predict_genre(data, clf):
    return clf.predict([data])[0]


def main():
    logger.setLevel(logging.DEBUG)
    dynamic_loading.imports_from_modules(constants.DATA_CLEANERS_DIR)
    dynamic_loading.imports_from_modules(constants.FEAT_EXTS_DIR)
    clf = persistence.load(CLF_NAME)

    print("Guess Genre By Lyrics")

    if fetch_lyrics:
        artist = input(">Artist: ").lower()
        song = input(">Song: ").lower()
        lyric = fetch_lyrics.fetch("%s" % artist, "%s" % song)
    else:
        lyric = text_from_file.load(constants.SAMPLE_LYRIC_PATH)

    if lyric:
        prediction = predict_genre(lyric, clf)
        print('{}\n{}'.format('-' * 100, lyric))
        print('{}\nPrediction: {}'.format('-' * 100, prediction))

    else:
        print("No lyrics no prediction :(")

if __name__ == '__main__':
    main()
