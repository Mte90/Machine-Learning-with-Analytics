#!/usr/bin/env python3
import pandas as pd
import re

def sanitize_slug(slug):
    #.replace('/en/','').replace('/it/','')
    slug = slug.replace('-',' ').replace('  ',' ').replace('category','').replace('cero','').replace('there','').replace(' rc ',' ').replace(' with ','')
    slug = slug.replace('e/o',' ').replace('/',' ').replace('guest post','guest').replace('guest_post','guest').replace(' or','')
    slug = slug.replace(' to ',' ').replace(' and ',' ').replace(' an ',' ').replace(' by','').replace('was','').replace('its','').replace(' su ','')
    slug = re.sub('[0-9]+', ' ', slug)
    slug = re.sub(r'\?author=.*', '', slug)
    slug = re.sub(r'\?lang=.*', '', slug)
    slug = re.sub(r'\b\w{1,1}\b', ' ', slug)
    slug = slug.replace('  ','').strip()
    if slug is '':
        return 'mancante'
    return slug 

df=pd.read_csv('./analytics.csv', engine='python') # skiprows=1,

print("CSV caricato")

df['Pagina'] = df['Pagina'].apply(sanitize_slug)
df = df.dropna()
del df['Visualizzazioni di pagina uniche']
del df['Tempo medio sulla pagina']
del df['Frequenza di rimbalzo']
del df['% uscita']
#df = df.groupby('Pagina', as_index=False).agg(lambda x:x.value_counts().index[0]) # rimuove quelli con la stessa pagina anche se con valori diversi
df = df.groupby('Pagina', as_index=False).aggregate({'Visualizzazioni di pagina': 'sum', 'Accessi': 'sum'}).reindex(columns=df.columns)
print("CSV pulito")

df.to_csv('analytics_parsed.csv')