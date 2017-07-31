import constants
from utils.logger import logger
from fuzzywuzzy import process


def get_parent_genre(found_genre):
    tokens_list = constants.WORD_TOKENIZER.tokenize(found_genre)
    found_genre = ' '.join(tokens_list)

    # Get the closest matching listed genre, and a similarity score
    if not found_genre:
        decided_genre = constants.DEFAULT_GENRE
        closest_genre = ''
        score = 0
    else:
        closest_genre, score = process.extractOne(found_genre,
                                                  constants.ALL_GENRES_LIST)

        if score > constants.GENRE_SIMILARITY_THRESHOLD:
            parent_genre = constants.GENRES_TREE[closest_genre]
            decided_genre = parent_genre
        else:
            decided_genre = constants.DEFAULT_GENRE

    return decided_genre, closest_genre, score


def normalize_genres(df, col_name):
    df[col_name] = df[col_name].apply(lambda genre: get_parent_genre(genre)[0])
    logger.info("Normalized data in column %s" % col_name)
    return df

if __name__ == '__main__':
    result_tup = get_parent_genre("drum'n'bass")
    logger.debug('Closest: {} , Decided: {} , Score: {} '.format(*result_tup))
