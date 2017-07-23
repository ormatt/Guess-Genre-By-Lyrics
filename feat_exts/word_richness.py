"""
Character repetitions ratio
"""
import os
from base_feat_ext import BaseFeatExt
from utils.feat_exts_aux import TOKENIZER


class Worker(BaseFeatExt):
    def __init__(self, sample_col_name=None):
        super(self.__class__, self).__init__(sample_col_name)
        self.feature_name = os.path.splitext(os.path.basename(__file__))[0]

    @staticmethod
    def extract(text):
        tokens = TOKENIZER.tokenize(text)
        tokens_len = max(1, len(tokens))
        return float(len(set(tokens))) / tokens_len
