import constants as const
from utils.logger import logger
ENG_RATIO = 0.75
MIN_WORD_COUNT = 10


def check_ratio(text, blacklist, whitelist):
    total_count = 0
    eng_count = 0

    for element in text:
        if element in blacklist:
            continue

        total_count += 1
        if element in whitelist:
            eng_count += 1

    if total_count == 0:
        return False

    ratio = eng_count / float(total_count)

    if ratio < ENG_RATIO:
        return False
    else:
        return True


def eng_words_ratio(tokens):
    # Method is not reliable when number of tokens is too small
    if len(tokens) < MIN_WORD_COUNT:
        return True
    return check_ratio(tokens, [], const.ENGLISH_CORPUS)


def eng_chars_ratio(text):
    return check_ratio(text, const.DIGITS_SYMBOLS, const.ENG_CHARS)


def is_valid_english(text):
    text = text.lower()
    tokens = const.WORD_TOKENIZER.tokenize(text)

    if eng_chars_ratio(text) is False:
        return False
    else:
        return eng_words_ratio(tokens)


def clean(df, _=None):
    map(lambda col: df[df[col].map(lambda x: is_valid_english(x))],
        df.columns.values)
    return df
