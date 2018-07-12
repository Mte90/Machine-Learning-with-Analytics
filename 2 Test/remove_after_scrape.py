#!/usr/bin/env python3
import pandas as pd

df=pd.read_csv('./analytics_content.csv', engine='python')
df = df[df['Pagina'] != '']
df.drop('Unnamed: 0.1', axis=1, inplace=True)
df.dropna()
df.to_csv('analytics_ready.csv', index=False)
print("CSV pulito nuovamente")
