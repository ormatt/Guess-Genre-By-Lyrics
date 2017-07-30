from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn import tree
from transformers import describe_data
from utils.dynamic_loading import objects_from_modules as get_objs

from constants import FEAT_EXTS_DIR


def get_pipeline(sample_col, parallel_jobs=None):
    feat_ext_objs = [feat_ext_class(sample_col)
                     for feat_ext_class in get_objs(FEAT_EXTS_DIR, 'Worker')]

    feat_ext_tuples = [(feat_ext_obj.feature_name, feat_ext_obj)
                       for feat_ext_obj in feat_ext_objs]

    pipeline = Pipeline([
        ('features', FeatureUnion(feat_ext_tuples, n_jobs=parallel_jobs)),
        ('describe_data', describe_data.Transformer()),
        ('classifier', tree.DecisionTreeClassifier(max_depth=20)),
    ])
    return pipeline
