import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

from utils.logger import logger


class Transformer(BaseEstimator, TransformerMixin):
    @staticmethod
    def describe(elem):
        try:
            if elem is None or len(elem) == 0:
                return
        except Exception as ex:
            logger.error("%s could not use len method - %s" %
                         (__name__,
                          ex))
            return

        logger.debug("Type is: {}".format(type(elem)))

        if isinstance(elem, np.ndarray):
            logger.debug("numpy ndarray shape is: {}".format(elem.shape))
        elif isinstance(elem, pd.DataFrame):
            logger.debug("df columns: {}".format(elem.columns.values))
            logger.debug("df info: {}".format(elem.info()))

    @staticmethod
    def unpack_and_describe(elems):
        if not isinstance(elems, tuple):
            Transformer.describe(elems)
            return elems,

        if len(elems) == 0:
            return ()

        return (Transformer.unpack_and_describe(elems[0]) +
                Transformer.unpack_and_describe(elems[1:]))

    def transform(self, elems, _=None):
        if isinstance(elems, np.ndarray):
            self.describe(elems)

        else:
            for elem in elems:
                self.unpack_and_describe(elem)

        return elems

    def fit(self, X, _=None):
        return self

    def score(*args):
        pass

    def predict(*args):
        pass
