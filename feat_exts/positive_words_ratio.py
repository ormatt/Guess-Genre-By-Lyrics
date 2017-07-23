"""
Character repetitions ratio
"""
import os
from base_feat_ext import BaseFeatExt
from constants import POSITIVE_WORDS_PATH
from utils.feat_exts_aux import extract_set_words_ratio, read_lines_into_set

POSITIVE_WORDS_SET = read_lines_into_set(POSITIVE_WORDS_PATH)

class Worker(BaseFeatExt):
    def __init__(self, sample_col_name=None):
        super(self.__class__, self).__init__(sample_col_name)
        self.feature_name = os.path.splitext(os.path.basename(__file__))[0]

    @staticmethod
    def extract(text):
        return extract_set_words_ratio(text, POSITIVE_WORDS_SET)