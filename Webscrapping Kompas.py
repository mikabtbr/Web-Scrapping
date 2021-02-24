from bs4 import BeautifulSoup
import requests
import json
import pandas as pd

def kompas():

    url=  "https://www.kompas.com/"
    web = requests.get(url)
    out = BeautifulSoup(web.content, 'html.parser')


    berita = out.find_all("h4",{"class":"most__title"})
    # print(berita)   


    for name in berita:
        allchar = []
        allchar.append(name.text)
    # print(allchar)


    df = pd.DataFrame({'Judul Berita Terpopuler':allchar})
    df.index +=1
    print(df.head())
    

    
kompas()
    
    