#!/usr/bin/env python3

import pandas as pd
from keras.preprocessing.text import Tokenizer
from keras.models import Sequential
from keras.layers import Dense, Dropout
from sklearn.preprocessing import RobustScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from yellowbrick.regressor import ResidualsPlot
import numpy as np

df=pd.read_csv('./analytics_parsed.csv', engine='python') 

print("CSV caricato")

rscaler = RobustScaler()
tokenizer = Tokenizer()
tokenizer.fit_on_texts(df['Pagina'])
X = tokenizer.texts_to_matrix(df['Pagina'], mode='count')
y = rscaler.fit_transform(df['Visualizzazioni di pagina'].values.reshape(-1, 1))
print("Tonekizer caricato")

# salvo gli errori
model = LinearRegression()
model.fit(X, y)
dati = model.predict(X)
df['Errors'] = dati
df.drop(df.columns[[0]], axis=1, inplace=True)
df.sort_values('Errors').to_csv('X.csv')
print('Errori salvati')

def linearregression(X, y):
    model = LinearRegression()
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.5)
    model.fit(X_train, y_train)
    
    #model = Sequential([
    #    Dense(800, input_shape=(10000,), activation='relu'),
    #    Dropout(0.5),
    #    Dense(1, activation='linear')
    #])
    #model.compile(metrics=['mse'], optimizer='rmsprop',loss='mse')
    #model.fit(X_train, y_train,
    #          validation_data=[X_test, y_test],
    #          epochs=20
    #)
    
    predict = model.predict(X_test)
    test_score = r2_score(y_test, predict)
    
    training = model.predict(X_train)
    training_score = r2_score(y_train, training)
    print('Training score', training_score)
    print('Test score', test_score)

# dove si trova l'errore

linearregression(X, y)
linearregression(X, y)
linearregression(X, y)

#ridge = Ridge()
#visualizer = ResidualsPlot(ridge)
#visualizer.fit(X_train, y_train)  # Fit the training data to the visualizer
#visualizer.score(X_test, y_test)  # Evaluate the model on the test data
#g = visualizer.poof()