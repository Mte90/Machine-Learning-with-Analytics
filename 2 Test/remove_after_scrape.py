#!/usr/bin/env python3
import pandas as pd
import numpy as np

df=pd.read_csv('./analytics_content.csv')
df['Pagina'].replace('', np.nan, inplace=True)
df.drop('Unnamed: 0.1', axis=1, inplace=True)
df.dropna(subset=['Pagina'], inplace=True)
df.drop('Unnamed: 0', axis=1, inplace=True)
df.to_csv('analytics_ready.csv')
print("CSV pulito nuovamente")
