#!/usr/bin/env python3
import os
from keras.models import load_model
from sklearn.metrics import r2_score
from sklearn.preprocessing import RobustScaler
import numpy as np
np.random.seed(1)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


def evaluate(X, name):
    model = load_model(name + '.h5')
    rscaler = RobustScaler()
    X = rscaler.fit_transform(np.array(X).reshape(-1, 1))
    predict = model.predict(X)

    score = r2_score(X, predict)
    print(name + ' Score', score)


evaluate('firefox', 'view')
evaluate('firefox', 'access')
