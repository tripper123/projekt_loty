
import glob
import pandas as pd
from IPython.display import HTML
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from unicodedata import normalize

# names = ['data' , 'lotnisko wylotu', 'lotnisko przylotu', 'linia lotnicza']
# df = pd.read_excel('../data/dane.xlsx', names=names)
#
# df['rok']=df['data']
#
# df['rok'] = df['data'].dt.year
#
# linie = df.groupby('linia lotnicza')['linia lotnicza'].count().sort_values(ascending=0).head(10).reset_index(name="ilość lotów")
# lata = df.groupby('rok')['rok'].count().sort_values(ascending=0).head(10).reset_index(name="ilość lotów")
# lotnisko_wylotu = df.groupby('lotnisko wylotu')['lotnisko wylotu'].count().sort_values(ascending=0).head(10).reset_index(name="ilość wylotów")
# lotnisko_przylotu = df.groupby('lotnisko przylotu')['lotnisko przylotu'].count().sort_values(ascending=0).head(10).reset_index(name="ilość przylotów")
# lotnisko = (df.groupby('lotnisko przylotu')['lotnisko przylotu'].count()+
#             df.groupby('lotnisko wylotu')['lotnisko wylotu'].count()).sort_values(ascending=0).head(10).reset_index(name="ilość wylotów/przylotów")
#
#
# print(df)
# print(df.head(3))
# print(linie)
# print(lata)
# print(lata)
# print(lotnisko_wylotu)
# print(lotnisko_przylotu)
# print(lotnisko)
# html = pd.DataFrame(linie).to_html()
# html2 = pd.DataFrame(lata).to_html()
# html3 = pd.DataFrame(lotnisko_wylotu).to_html()
# html4 = pd.DataFrame(lotnisko_przylotu).to_html()
# html5 = pd.DataFrame(lotnisko).to_html()
#
# # write html to file
# text_file = open("templates/index2.html", "w")
# text_file.write(html)
# text_file.write(html2)
# text_file.write(html3)
# text_file.write(html4)
# text_file.write(html5)
#
# text_file.close()

def create_reports(folder_path: str):
    names = ['data', 'lotnisko wylotu', 'lotnisko przylotu', 'linia lotnicza','cena']

    df = pd.read_excel('../data/dane1.xlsx', names=names)
    df['rok'] = df['data']
    df['rok'] = df['data'].dt.year
    df['cena'] = df['cena'].astype(int)


    linie = df.groupby('linia lotnicza')['linia lotnicza'].count().sort_values(ascending=0).head(10)


    lata = df.groupby('rok')['rok'].count().sort_values(ascending=0).head(10)

    lotnisko_wylotu = df.groupby('lotnisko wylotu')['lotnisko wylotu'].count().sort_values(ascending=0).head(
        10)
    lotnisko_przylotu = df.groupby('lotnisko przylotu')['lotnisko przylotu'].count().sort_values(ascending=0).head(
        10)
    lotnisko = ((df.groupby('lotnisko przylotu')['lotnisko przylotu'].count() +
                df.groupby('lotnisko wylotu')['lotnisko wylotu'].count()).sort_values(ascending=0).head(10))


    df1 = df.sort_values(by='cena', ascending=1).head(5)
    najtansze_loty = df1 [['data','lotnisko wylotu', 'lotnisko przylotu', 'cena']].set_index('data')
    df2 = df.sort_values(by='cena', ascending=0).head(5)
    najdrozsze_loty = df2[['data','lotnisko wylotu', 'lotnisko przylotu', 'cena']].set_index('data')


    html = pd.DataFrame(linie).to_html(classes='table table-stripped')
    html2 = pd.DataFrame(lata).to_html(classes='table table-stripped')
    html3 = pd.DataFrame(lotnisko_wylotu).to_html(classes='table table-stripped')
    html4 = pd.DataFrame(lotnisko_przylotu).to_html(classes='table table-stripped')
    html5 = pd.DataFrame(lotnisko).to_html(classes='table table-stripped')
    html6 = pd.DataFrame(najtansze_loty).to_html(classes='table table-stripped')
    html7 = pd.DataFrame(najdrozsze_loty).to_html(classes='table table-stripped')
    text_file = open("templates/index2.html", "w")
    text_file.write(html)
    '<td colspan="20" class="divider"><hr /></td>'
    text_file.write(html2)
    text_file.write(html3)
    text_file.write(html4)
    text_file.write(html5)
    text_file.write(html6)
    text_file.write(html7)
    text_file.close()

    sum = df['cena'].sum()
    srednia = df['cena'].mean().astype(int)
    print(sum)
    print(srednia)
create_reports('../data/dane1.xlsx')
