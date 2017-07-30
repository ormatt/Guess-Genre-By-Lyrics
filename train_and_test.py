import numpy as np
from sklearn.model_selection import KFold
import utils.persistence
from utils.logger import logger


def kfold(X, y, clf, splits=5):
    kf = KFold(n_splits=splits, shuffle=True)

    scores = []
    for k, (train, test) in enumerate(kf.split(X, y)):
        clf.fit(X[train], y[train])
        score = clf.score(X[test], y[test])
        logger.info("[Fold {0}] score: {1:.5f}".format(k, score))
        scores.append(score)

    utils.persistence.dump('clf_fitted', clf)
    scores_mean = np.mean(scores)
    return scores_mean
