#!/usr/bin/env python3
import pandas as pd
import numpy as np
import nltk

nltk.download('stopwords')
stop_english = nltk.corpus.stopwords.words('english')
stop_italian = nltk.corpus.stopwords.words('italian')

df=pd.read_csv('./analytics_content.csv')
df['Pagina'].replace('', np.nan, inplace=True)
df.drop('Unnamed: 0.1', axis=1, inplace=True)
df.dropna(subset=['Pagina'], inplace=True)
df.drop('Unnamed: 0', axis=1, inplace=True)
df['Pagina'] = df['Pagina'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_english)]))
df['Pagina'] = df['Pagina'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_italian)]))
df.to_csv('analytics_ready.csv')
print("CSV pulito nuovamente")
