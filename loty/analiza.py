

import pandas as pd
from IPython.display import HTML
import numpy as np
import matplotlib as mpl

names = ['data' , 'lotnisko wylotu', 'lotnisko przylotu', 'linia lotnicza']
df = pd.read_excel('../data/dane.xlsx', names=names)

df['rok']=df['data']

df['rok'] = df['data'].dt.year

linie = df.groupby('linia lotnicza')['linia lotnicza'].count().sort_values(ascending=0).head(5)
lata = df.groupby('rok')['rok'].count().sort_values(ascending=0).head(5)
lotnisko_wylotu = df.groupby('lotnisko wylotu')['lotnisko wylotu'].count().sort_values(ascending=0).head(5)
lotnisko_przylotu = df.groupby('lotnisko przylotu')['lotnisko przylotu'].count().sort_values(ascending=0).head(5)
print(df)
print(df.head(3))
print(linie)

print(lata)
print(lata)
print(lotnisko_wylotu)
print(lotnisko_przylotu)

html = pd.DataFrame(linie).to_html()
html2 = pd.DataFrame(lata).to_html()
html3 = pd.DataFrame(lotnisko_wylotu).to_html()
html4 = pd.DataFrame(lotnisko_przylotu).to_html()
# write html to file
text_file = open("templates/index2.html", "w")
text_file.write(html)
text_file.write(html2)
text_file.write(html3)
text_file.write(html4)
text_file.close()