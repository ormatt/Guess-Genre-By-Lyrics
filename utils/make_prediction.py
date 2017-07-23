from __future__ import print_function
from utils import persistence
clf = persistence.load('clf_fitted_score')


def predict():
    print('Prediction: %s' % clf.predict([l]))


l = """
Data is everything
But it is not a sun
Nor is it the wind

What is like the wind
In a hot afternoon

Like the wind
Like the wind
Like the W-I-N-D

What is like a sun
In a chilly afternoon

Like a sun
Like a sun
Like a S-U-N

Data is everything

"""

predict()
