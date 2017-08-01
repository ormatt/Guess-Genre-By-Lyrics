from __future__ import print_function
import os

import constants
from utils import dynamic_loading, persistence, text_from_file

SELF_DIR = os.path.dirname(os.path.abspath(__file__))

CLF_NAME = constants.CLF_FITTED_DUMP_NAME


def predict_genre(data, clf):
    return clf.predict([data])


def main():
    dynamic_loading.imports_from_modules(constants.DATA_CLEANERS_DIR)
    dynamic_loading.imports_from_modules(constants.FEAT_EXTS_DIR)

    clf = persistence.load(CLF_NAME)
    lyric = text_from_file.load(constants.SAMPLE_LYRIC_PATH)
    print('Prediction: %s' % predict_genre(lyric, clf))

if __name__ == '__main__':
    main()
