import numpy as np
from constants import WORD_TOKENIZER


def clean(df, _=None):
    for col in df.columns.values:
        df['text_len'] = df[col].str.len()
        df['tokens_num'] = df[col].apply(lambda x:
                                         len(WORD_TOKENIZER.tokenize(x)))
        avg_col_text_len = np.mean(df['text_len'])
        avg_col_tokens_num = np.mean(df['tokens_num'])
        df = df[df['text_len'] > avg_col_text_len/100]
        df = df[df['tokens_num'] > avg_col_tokens_num / 100]
    return df
