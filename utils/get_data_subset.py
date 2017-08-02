import numpy as np

from utils.logger import logger

def crop(df, nrows=None, cols=None):
    if nrows is not None:
        df = df[:nrows]
    if cols is not None:
        df = df[cols]

    return df


def filter_rows_by_string(df, cols, strings, action='keep'):
    rows_count = len(df)

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


def get_x_y(df, sample_col_name, target_col_name):
    """
    Get samples data and target (truth) data as numpy ndarray.
    Args:
        df: Pandas DataFrame
        sample_col_name: Samples column name in df
        target_col_name: Targets column name in df

    Returns:

    """
    X = df[sample_col_name].values
    y = df.loc[:, target_col_name].values
    return X, y
