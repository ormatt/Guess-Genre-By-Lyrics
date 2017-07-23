"""
Character repetitions ratio
"""
import os
from base_feat_ext import BaseFeatExt
from utils.feat_exts_aux import TOKENIZER_LINE_SENTENCES


class Worker(BaseFeatExt):
    def __init__(self, sample_col_name=None):
        super(self.__class__, self).__init__(sample_col_name)
        self.feature_name = os.path.splitext(os.path.basename(__file__))[0]

    @staticmethod
    def extract(text):
        total_count = 0
        capital_letters_count = 0
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if not line:
                continue

            split = TOKENIZER_LINE_SENTENCES.split(line)
            for sentence in split:
                sentence = sentence.strip()
                if len(sentence) <= 1:
                    continue
                words = sentence.split(' ')[1:]
                for word in words:
                    total_count += 1
                    if len(word) <= 1 or word.lower() == "i'm":
                        continue
                    if word[0].isupper():
                        capital_letters_count += 1

        try:
            return float(capital_letters_count) / total_count
        except ZeroDivisionError:
            return 0.0
