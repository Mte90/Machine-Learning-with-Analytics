#!/usr/bin/env python3
import pandas as pd
import re, os

def sanitize_slug(slug):
    slug = re.sub(r'\?author=.*', '', slug)
    slug = re.sub(r'\?lang=.*', '', slug)
    slug = re.sub(r'\?author=.*', '', slug)
    slug = slug.replace('  ', '').replace('guest_post', 'guest-post').strip()
    slug = os.path.basename(os.path.normpath(slug))
    if slug is '' or len(slug) < 3:
        return ''
    return slug


df=pd.read_csv('./analytics.csv', engine='python')
print("CSV caricato")

df['Pagina'] = df['Pagina'].apply(sanitize_slug)
df.to_csv('analytics_parsed.csv')
print("CSV pulito")
print(str(df.shape[0]) + " righe")