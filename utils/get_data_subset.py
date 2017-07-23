from utils.logger import logger


def crop(df, nrows=None, cols=None):
    if nrows is not None:
        df = df[:nrows]
    if cols is not None:
        df = df[cols]

    return df


def filter_rows_by_string(df, cols, strings, action='keep'):
    rows_count = len(df)
    logger.debug('Row count is {}'.format(rows_count))

    for col in cols:
        if action.lower() == 'remove':
            df = df[~df[col].isin(strings)]
        elif action.lower() == 'keep':
            df = df[df[col].isin(strings)]
        else:
            logger.error("Filter action unsupported. Skipping.")

    logger.debug('Row count is {} '
                 '(Filtered out {} rows)'.format(len(df),
                                                 rows_count - len(df)))
    return df
