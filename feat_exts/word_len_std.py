"""
Character repetitions ratio
"""
import os
import numpy as np
from base_feat_ext import BaseFeatExt
from utils.feat_exts_aux import TOKENIZER


class Worker(BaseFeatExt):
    def __init__(self, sample_col_name=None):
        super(self.__class__, self).__init__(sample_col_name)
        self.feature_name = os.path.splitext(os.path.basename(__file__))[0]

    @staticmethod
    def extract(text):
        tokens = TOKENIZER.tokenize(text)
        lengths = [len(word) for word in tokens]
        return np.std(lengths)
