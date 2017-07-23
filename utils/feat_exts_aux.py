from re import compile
from nltk import RegexpTokenizer

TOKENIZER = RegexpTokenizer(r'''[a-zA-Z][a-zA-Z']+[a-zA-Z]+|[a-zA-Z]+''')
TOKENIZER_LINE_SENTENCES = compile('''([.?!])''')


def extract_set_words_ratio(text, words_set):
    count = 0
    tokens = TOKENIZER.tokenize(text)
    for token in tokens:
        token = token.strip()
        if token and token.lower() in words_set:
            count += 1
    tokens_len = max(1, len(tokens))
    return float(count) / tokens_len


def read_lines_into_set(file_path):
    words_set = set()
    with open(file_path, 'r') as reader:
        for line in reader:
            word = line.strip().lower()
            if word:
                words_set.add(word)
    return words_set
