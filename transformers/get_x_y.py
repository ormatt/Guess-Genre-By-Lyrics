import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class GetXY(BaseEstimator, TransformerMixin):
    def __init__(self, target_col_name, sample_col_name, features_names, output_type='ndarray', target_exists=True):
        self.target_col_name = target_col_name
        self.sample_col_name = sample_col_name
        self.features_names = features_names
        self.output_type = output_type
        self.target_exists = target_exists

    def transform(self, ndarray, y=None):
        """Return a series"""

        if self.output_type.lower() == 'ndarray':
            if self.target_exists:
                X = ndarray[:, :-1]
                y = ndarray[:, -1] if y is None else y
            else:
                X = ndarray

        elif self.output_type.lower() == 'dataframe':
            if self.target_exists:
                X = pd.DataFrame(data=ndarray[:, :-1],
                                 columns=self.features_names[0: len(self.features_names) - 1],
                                 dtype=float)

                y = pd.DataFrame(data=ndarray[:, -1],
                                 columns=[self.target_col_name],
                                 dtype=float) if y is None else y
            else:
                X = pd.DataFrame(data=ndarray[:, :],
                                 columns=self.features_names,
                                 dtype=float)
        else:
            X = ndarray

        return X, y

    def fit(self, X, y=None):
        return self
