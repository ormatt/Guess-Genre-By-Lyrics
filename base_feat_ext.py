import abc
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from utils.logger import logger


class BaseFeatExt(BaseEstimator, TransformerMixin):
    def __init__(self, sample_col_name, target_col_name=None):
        self.sample_col_name = sample_col_name
        self.feature_name = None
        self.target_col_name = target_col_name

    __metaclass__ = abc.ABCMeta

    @staticmethod
    @abc.abstractmethod
    def extract(sample):
        """Implement this"""

    def transform(self, df, _=None):
        logger.info("Extracting feature %s" % self.feature_name)
        return np.array([[self.extract(i)] for i in df])

    def fit(self, *_):
        return self
