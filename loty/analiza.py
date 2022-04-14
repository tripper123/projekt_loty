

import pandas as pd


names = ['data' , 'lotnisko wylotu', 'lotnisko przylotu', 'linia lotnicza']
df = pd.read_excel('../data/dane.xlsx', names=names)

df['rok']=df['data']

df['rok'] = df['data'].dt.year

linie = df.groupby('linia lotnicza')['linia lotnicza'].count().sort_values(ascending=0)
lata = df.groupby('rok')['rok'].count().sort_values(ascending=0)
lotnisko_wylotu = df.groupby('lotnisko wylotu')['lotnisko wylotu'].count().sort_values(ascending=0)
lotnisko_przylotu = df.groupby('lotnisko przylotu')['lotnisko przylotu'].count().sort_values(ascending=0)
print(df)

print(linie)

print(lata)

print(lotnisko_wylotu)
print(lotnisko_przylotu)
