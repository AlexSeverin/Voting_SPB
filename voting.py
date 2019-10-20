'''
#from pathlib import Path
#import requests
#BASE_URL = 'http://www.st-petersburg.vybory.izbirkom.ru/region/region/st-petersburg?action=show&tvd=27820001217417&vrn=27820001217413&region=78&global=&sub_region=78&prver=0&pronetvd=null&vibid=27820001217430&type=222'
#r = requests.get(BASE_URL)
#soap = BeautifulSoup(r.text, "html.parser")
#print(soap.title)
'''

'''
import bs4 as bs
import urllib.request

source = urllib.request.urlopen('http://www.st-petersburg.vybory.izbirkom.ru/region/region/st-petersburg?action=show&tvd=27820001217417&vrn=27820001217413&region=78&global=&sub_region=78&prver=0&pronetvd=null&vibid=27820001217430&type=222').read()
soup = bs.BeautifulSoup(source,'lxml')

table = soup.find('table', style="padding-left: 3px; padding-right: 3px;")

table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)
'''

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

dfs = pd.read_html('http://www.st-petersburg.vybory.izbirkom.ru/region/region/st-petersburg?action=show&tvd=27820001217417&vrn=27820001217413&region=78&global=&sub_region=78&prver=0&pronetvd=null&vibid=27820001217430&type=222',header=0,encoding='cp1251')
for df in dfs:
#    print(df)
#    df.reset_index(inplace=True)
    print(df.head())

style.use('fivethirtyeight')

df['УИК №1725'].plot()
plt.legend()
plt.show()