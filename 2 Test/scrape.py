#!/usr/bin/env python3
import pandas as pd
import re, os
import requests

def sanitize_slug(slug):
    slug = re.sub(r'\?author=.*', '', slug)
    slug = re.sub(r'\?lang=.*', '', slug)
    slug = re.sub(r'\?author=.*', '', slug)
    slug = slug.replace('  ', '').replace('guest_post', 'guest-post').strip()
    slug = os.path.basename(os.path.normpath(slug))
    if slug is '' or len(slug) < 3:
        return 'mancante'
    return slug


def download_content(slug):
    global count
    count += 1
    print(' Parsed ' + str(count) + ': ' + slug)
    req = requests.get(url='https://daniele.tech/wp-json/wp/v2/posts?slug=' + slug)
    for item in req.json():
        content = item['content']['rendered']
        content = re.compile(r'<[^>]+>').sub('', content).replace('&#8217;',"'").replace('&#8211;',"-").replace('&#8221;','"')
        return content

count = 0
df=pd.read_csv('./analytics.csv', engine='python')
print("CSV caricato")

df['Pagina'] = df['Pagina'].apply(sanitize_slug)
df = df.dropna()
del df['Visualizzazioni di pagina uniche']
del df['Tempo medio sulla pagina']
del df['Frequenza di rimbalzo']
del df['% uscita']
df = df.groupby('Pagina', as_index=False).aggregate({'Visualizzazioni di pagina': 'sum', 'Accessi': 'sum'}).reindex(columns=df.columns)
#df = df.groupby('Pagina', as_index=False).agg(lambda x:x.value_counts().index[0])
df.to_csv('analytics_parsed.csv')
print("CSV pulito")
print(str(df.shape[0]) + " righe")

df['Pagina'] = df['Pagina'].apply(download_content)
df = df[df['Pagina'] == '']
print(str(df.shape[0]) + " righe")
df.to_csv('analytics_content.csv')
print("CSV riempito")
