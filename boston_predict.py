import numpy as np
from sklearn.externals import joblib

class PredictBostonData(object):
    def __init__(self, lstat, crir, age):
        self.data = np.array([lstat, crir, age]).reshape(1,3)

    def predict(self):
        clf = joblib.load('/Users/takahashikoji/Downloads/linear.pkl')
        return clf.predict(self.data)
