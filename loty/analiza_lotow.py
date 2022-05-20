
import glob
import pandas as pd
from IPython.display import HTML
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from unicodedata import normalize

def create_reports(folder_path: str):
    names = ['data', 'lotnisko wylotu', 'lotnisko przylotu', 'linia lotnicza','cena']
    df = pd.read_excel('../data/dane1.xlsx', names=names)
    df['rok'] = df['data']
    df['rok'] = df['data'].dt.year
    df['cena'] = df['cena'].astype(int)
    linie = df.groupby('linia lotnicza')['linia lotnicza'].count().sort_values(ascending=0).head(10)\
        .to_frame().rename(columns ={'linia lotnicza':'ilość lotów'})
    lata = df.groupby('rok')['rok'].count().sort_values(ascending=0).head(10)\
        .to_frame().rename(columns ={'rok':'ilość lotów'})
    lotnisko_wylotu = df.groupby('lotnisko wylotu')['lotnisko wylotu']\
        .count().sort_values(ascending=0).head(
        10).to_frame().rename(columns ={'lotnisko wylotu':'ilość wylotów'})
    lotnisko_przylotu = df.groupby('lotnisko przylotu')['lotnisko przylotu']\
        .count().sort_values(ascending=0).head(
        10).to_frame().rename(columns ={'lotnisko przylotu':'ilość przylotów'})

    df1 = df.sort_values(by='cena', ascending=1).head(5)
    najtansze_loty = df1 [['data','lotnisko wylotu', 'lotnisko przylotu', 'cena']].set_index('data')
    df2 = df.sort_values(by='cena', ascending=0).head(5)
    najdrozsze_loty = df2[['data','lotnisko wylotu', 'lotnisko przylotu', 'cena']].set_index('data')
    html = pd.DataFrame(linie).to_html(classes='table table-striped text-center', justify='center')
    html2 = pd.DataFrame(lata).to_html(classes='table table-striped text-center', justify='center')
    html3 = pd.DataFrame(lotnisko_wylotu).to_html(classes='table table-striped text-center', justify='center')
    html4 = pd.DataFrame(lotnisko_przylotu).to_html(classes='table table-striped text-center', justify='center')
    html6 = pd.DataFrame(najtansze_loty).to_html(classes='table table-striped text-center', justify='center')
    html7 = pd.DataFrame(najdrozsze_loty).to_html(classes='table table-striped text-center', justify='center')

    text_file = open("templates/analiza_do_html.html", "w")
    text_file.write("Najpopularniejsze linie lotnicze")
    text_file.write(html)
    text_file.write("Lata z największą liczbą lotów")
    text_file.write(html2)
    text_file.write("Lotniska z największą liczbą wylotów")
    text_file.write(html3)
    text_file.write("Lotniska z największą liczbą przylotów")
    text_file.write(html4)
    text_file.write("Lista najtańszych lotów")
    text_file.write(html6)
    text_file.write("Lista najdroższych lotów")
    text_file.write(html7)
    text_file.close()
create_reports('../data/dane1.xlsx')
