import os
import string

from nltk import RegexpTokenizer

import utils.corpora
import utils.genres_tree

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, 'data')
DATA_PATH = os.path.join(DATA_DIR, 'dev_genres_lyrics.json')
if not os.path.isfile(DATA_PATH):
    DATA_PATH = os.path.join(DATA_DIR, 'genres_lyrics.json')

RESOURCES_DIR = os.path.join(SCRIPT_DIR, 'resources')
FEAT_EXTS_DIR = os.path.join(SCRIPT_DIR, 'feat_exts')
DATA_CLEANERS_DIR = os.path.join(SCRIPT_DIR, 'data_cleaners')
DUMPS_DIR = os.path.join(SCRIPT_DIR, 'dumps')

GENRES_TREE_PATH = os.path.join(RESOURCES_DIR, 'genres_tree.json')
GENRES_TREE, ALL_GENRES_LIST = utils.genres_tree.build(GENRES_TREE_PATH)

CUSTOM_CORPUS_MIN_LEN = 4
CUSTOM_CORPUS_PATH = os.path.join(RESOURCES_DIR, 'ud_dev_corpus.txt')
ENGLISH_CORPUS = utils.corpora.build(path=CUSTOM_CORPUS_PATH,
                                     min_len=CUSTOM_CORPUS_MIN_LEN)

if not os.path.isfile(CUSTOM_CORPUS_PATH):
    CUSTOM_CORPUS_PATH = os.path.join(RESOURCES_DIR, 'custom_corpus.txt')
ENG_CHARS = set(string.ascii_lowercase)

BAD_WORDS_PATH = os.path.join(RESOURCES_DIR, 'bad_words.txt')
POSITIVE_WORDS_PATH = os.path.join(RESOURCES_DIR, 'positive_words.txt')
NATURE_WORDS_PATH = os.path.join(RESOURCES_DIR, 'nature_words.txt')
NEGATIVE_WORDS_PATH = os.path.join(RESOURCES_DIR, 'negative_words.txt')

MODULE_PATTERN = '[a-zA-Z0-9][a-zA-Z0-9_]*.py'

SYMBOLS = {'~', '!', '@', '#', '$', '%', '^',
           "'", '"', '&', '*', '(', ')', '_',
           '+', ' ', '\n', '\\', '\r', '-',
           '=', '<', '>', '/', ',', '.', '[',
           ']', '{', '}', '|', ';', ':', '`'}

DIGITS = set(string.digits)
DIGITS_SYMBOLS = SYMBOLS.union(DIGITS)

WORD_TOKENIZER = RegexpTokenizer(r"[a-zA-Z][a-zA-Z']+[a-zA-Z]+|[a-zA-Z]+")

DEFAULT_GENRE = 'Other'

GENRE_SIMILARITY_THRESHOLD = 70
