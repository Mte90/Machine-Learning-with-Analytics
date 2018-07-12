#!/usr/bin/env python3
import pandas as pd

df=pd.read_csv('./analytics_content.csv', engine='python')
print("CSV caricato")

df = df.dropna()
df = df.groupby('Pagina', as_index=False).aggregate({'Visualizzazioni di pagina': 'sum', 'Accessi': 'sum'}).reindex(columns=df.columns)
df = df.drop(df.columns[0], axis=1)
df = df[df['Pagina'] != '']

df.to_csv('analytics_ready.csv')
print("CSV pulito nuovamente")
