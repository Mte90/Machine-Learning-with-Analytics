#!/usr/bin/env python3

import pandas as pd
from keras.preprocessing.text import Tokenizer
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout
from sklearn.preprocessing import RobustScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import numpy as np
np.random.seed(1)
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

def evaluate(X, name):
    model = load_model(name + '.h5')
    predict = model.predict(X)
    
    score = r2_score(X, predict)
    print(name + ' Score', score)

evaluate('firefox', 'view')
evaluate('firefox', 'access')
