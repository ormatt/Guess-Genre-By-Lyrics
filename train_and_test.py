import numpy as np
from sklearn.model_selection import KFold
import utils.persistence
from utils.logger import logger
from constants import CLF_KFOLD_DUMP_NAME, CLF_FITTED_DUMP_NAME


def test_using_kfold(X, y, clf, splits=5):
    kf = KFold(n_splits=splits, shuffle=True)

    scores = []
    for k, (train, test) in enumerate(kf.split(X, y)):
        logger.info("Fitting and transforming the model on one fold")
        clf.fit(X[train], y[train])
        score = clf.score(X[test], y[test])
        logger.info("[Fold {0}] score: {1:.5f}".format(k+1, score))
        scores.append(score)

    utils.persistence.dump(CLF_KFOLD_DUMP_NAME, clf)
    scores_mean = np.mean(scores)
    logger.info("Score: {}".format(scores_mean))
    return clf


def train_and_dump(X, y, clf):
    logger.info("Fitting and transforming the model")
    clf.fit(X, y)
    utils.persistence.dump(CLF_FITTED_DUMP_NAME, clf)
    return clf
