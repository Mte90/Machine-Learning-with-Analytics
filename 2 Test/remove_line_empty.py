#!/usr/bin/env python3
import pandas as pd

df=pd.read_csv('./analytics_content.csv', engine='python')
print("CSV caricato")

df = df[df['Pagina'] == '']

df.to_csv('analytics_content_ready.csv')
print("CSV riempito")
