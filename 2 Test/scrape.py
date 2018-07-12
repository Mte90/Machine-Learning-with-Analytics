#!/usr/bin/env python3
import pandas as pd
import re
import requests


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

df['Pagina'] = df['Pagina'].apply(download_content)
print(str(df.shape[0]) + " righe")
df.to_csv('analytics_content.csv')
print("CSV riempito")
