"""
Character repetitions ratio
"""
import os
from base_feat_ext import BaseFeatExt


class Worker(BaseFeatExt):
    def __init__(self, sample_col_name=None):
        super(self.__class__, self).__init__(sample_col_name)
        self.feature_name = os.path.splitext(os.path.basename(__file__))[0]

    @staticmethod
    def extract(text):
        text_len = max(len(text), 1)
        single_quote_count = max(text.count("'"), 1)
        return single_quote_count / float(text_len)
