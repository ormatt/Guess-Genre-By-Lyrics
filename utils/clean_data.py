from utils import dynamic_loading
from constants import DATA_CLEANERS_DIR
from utils.logger import logger


def execute_cleaners(df):
    cleaners = dynamic_loading.objects_from_modules(DATA_CLEANERS_DIR, 'clean')
    rows_count = len(df)
    for clean_func in cleaners:
        df = clean_func(df)
        logger.debug('Row count is {} '
                     '({} Cleaned {} rows)'.format(len(df),
                                                   clean_func.__module__,
                                                   rows_count - len(df)))
        rows_count = len(df)
    return df





