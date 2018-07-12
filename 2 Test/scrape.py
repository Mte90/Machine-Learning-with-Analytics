#!/usr/bin/env python3
import pandas as pd
import re, os
import requests

def sanitize_slug(slug):
    slug = re.sub(r'\?author=.*', '', slug)
    slug = re.sub(r'\?lang=.*', '', slug)
    slug = re.sub(r'\?author=.*', '', slug)
    slug = slug.replace('  ', '').replace('//', '').replace('guest_post', 'guest-post').strip()
    slug = os.path.basename(os.path.normpath(slug))
    if slug is '' or len(slug) < 3:
        return 'mancante'
    return slug


def download_content(slug):
    print('Parsed ' + slug)
    req = requests.get(url='https://daniele.tech/wp-json/wp/v2/posts?slug=' + slug)
    for item in req.json():
        content = item['content']['rendered']
        content = re.compile(r'<[^>]+>').sub('', content)
        return content

df=pd.read_csv('./analytics.csv', engine='python') # skiprows=1,
print("CSV caricato")

df['Pagina'] = df['Pagina'].apply(sanitize_slug)
df = df.dropna()
del df['Visualizzazioni di pagina uniche']
del df['Tempo medio sulla pagina']
del df['Frequenza di rimbalzo']
del df['% uscita']
df = df.groupby('Pagina', as_index=False).aggregate({'Visualizzazioni di pagina': 'sum', 'Accessi': 'sum'}).reindex(columns=df.columns)
df.to_csv('analytics_parsed.csv')
print("CSV pulito")
print(df.shape[0] + " righe")

df['Pagina'] = df['Pagina'].apply(download_content)
df.to_csv('analytics_content.csv')
print("CSV filled")