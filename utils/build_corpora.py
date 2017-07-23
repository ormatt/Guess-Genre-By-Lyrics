from nltk.corpus import words

import constants
from utils.funcs_registry import RegistryClass
from utils.logger import logger

@RegistryClass.corpus
def add_custom_corpus(eng_words_set):
    with open(constants.CUSTOM_CORPUS_PATH, 'r') as reader:
        for line in reader:
            line = line.strip()
            if len(line) >= constants.CUSTOM_CORPUS_MIN_LEN:
                eng_words_set.add(line)
    return eng_words_set


@RegistryClass.corpus
def add_nltk_words(eng_words_set):
    for word in words.words():
        eng_words_set.add(word)
    return eng_words_set


def build():
    words_set = set()
    for func in RegistryClass.get_funcs('corpus'):
        corpus_len_before = len(words_set)
        logger.debug("Executing function %s" % func.__name__)
        words_set = func(words_set)
        corpus_len = len(words_set)
        logger.debug("Added %d more words. Total is %d" %
                     (corpus_len - corpus_len_before, corpus_len))

    return words_set
