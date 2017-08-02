#!/usr/bin/env python3
from __future__ import absolute_import
import pandas as pd
import time

from utils.logger import logger
from constants import DATA_PATH, DF_DUMP_NAME, CLF_DUMP_NAME
import train_and_test
import model_pipeline
import utils.clean_data
import utils.persistence
import utils.normalize_data
import utils.get_data_subset

TARGET_COL = 'genre'
SAMPLE_COL = 'lyrics'


def main(mode="test"):
    start_time = time.time()
    logger.info("Started")
    df = pd.read_json(path_or_buf=DATA_PATH, orient='records', encoding="UTF8")
    logger.debug("Loaded {} rows into df".format(len(df)))
    df = utils.get_data_subset.crop(df, None, None)
    df = utils.get_data_subset.filter_rows_by_string(df,
                                                     [TARGET_COL],
                                                     ['Rock',
                                                      'Hip Hop'])
    df = utils.clean_data.execute_cleaners(df)
    df = utils.normalize_data.normalize_genres(df, TARGET_COL)
    X, y = utils.get_data_subset.get_x_y(df, SAMPLE_COL, TARGET_COL)

    clf = model_pipeline.get_pipeline(SAMPLE_COL)

    utils.persistence.dump(DF_DUMP_NAME, df)
    utils.persistence.dump(CLF_DUMP_NAME, clf)

    if mode.lower() == "test":
        train_and_test.test_using_kfold(X, y, clf)
    else:
        train_and_test.train_and_dump(X, y, clf)

    logger.info("Finished in {0:.2f} seconds".format(time.time() - start_time))

if __name__ == '__main__':
    main(mode="train")
