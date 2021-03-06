#!/usr/bin/env python3
import pandas as pd
import numpy as np

df=pd.read_csv('./analytics_parsed.csv', engine='python')
print("CSV caricato")

df = df.dropna()
del df['Visualizzazioni di pagina uniche']
del df['Tempo medio sulla pagina']
del df['Frequenza di rimbalzo']
del df['% uscita']
df = df.groupby('Pagina', as_index=False).aggregate({'Visualizzazioni di pagina': 'sum', 'Accessi': 'sum'}).reindex(columns=df.columns)
df = df.drop(df.columns[0], axis=1)
df['Pagina'].replace('', np.nan, inplace=True)
df.dropna(subset=['Pagina'], inplace=True)

df.to_csv('analytics_parsed.csv')
print("CSV pulito nuovamente")
