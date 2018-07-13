#!/usr/bin/env python3

import pandas as pd
from keras.preprocessing.text import Tokenizer
from keras.models import Sequential
from keras.layers import Dense, Dropout
from sklearn.preprocessing import RobustScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.linear_model import Ridge
from yellowbrick.regressor import ResidualsPlot
import numpy as np
np.random.seed(1)

def sequentialregression(X, y, name):
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.5)
    
    model = Sequential([
        Dense(800, input_shape=(16218,), activation='relu'),
        Dropout(0.5),
        Dense(1, activation='linear')
    ])
    model.compile(metrics=['mse'], optimizer='rmsprop',loss='mse')
    model.fit(X_train, y_train,
              validation_data=[X_test, y_test],
              epochs=20
    )
        
    predict = model.predict(X_test)
    test_score = r2_score(y_test, predict)
    
    training = model.predict(X_train)
    training_score = r2_score(y_train, training)
    print('Training score', training_score)
    print('Test score', test_score)
    np.savetxt('./' + name + '_X.txt', training)
    np.savetxt('./' + name + '_y.txt', predict)
    
#    ridge = Ridge()
#    visualizer = ResidualsPlot(ridge)
#    visualizer.fit(X_train, y_train)  # Fit the training data to the visualizer
#    visualizer.score(X_test, y_test)  # Evaluate the model on the test data
#    g = visualizer.poof()

df=pd.read_csv('./analytics_ready.csv', encoding = 'utf-8') 
df.drop(df.columns[[0]], axis=1, inplace=True)

print("CSV caricato")

rscaler = RobustScaler()
tokenizer = Tokenizer()
print(df['Pagina'])
tokenizer.fit_on_texts(df['Pagina'])
X = tokenizer.texts_to_matrix(df['Pagina'], mode='count')
y = rscaler.fit_transform(df['Visualizzazioni di pagina'].values.reshape(-1, 1))

sequentialregression(X, y, 'view')

y = rscaler.fit_transform(df['Accessi'].values.reshape(-1, 1))
sequentialregression(X, y, 'access')
