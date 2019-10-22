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
URL = 'http://www.st-petersburg.vybory.izbirkom.ru/region/region/st-petersburg?action=show&root=1&tvd=27820001217417&vrn=27820001217413&region=78&global=&sub_region=0&prver=0&pronetvd=null&vibid=27820001217417&type=222'

df1 = pd.read_html(URL,header=0,encoding='cp1251')[5].iloc[:, 1:].rename(columns={'Unnamed: 1':'Name'}) #Наименоване избирательной комиссии
print(df1)

df2 = pd.read_html(URL,encoding='cp1251')[6].iloc[:, 1:] #Территориальные избирательные комиссии с 1 по 30
print(df2)


#print(df2.loc[13])
#sudo apt-get install python3-tk

X = (df2.loc[1]).astype(int)
x=[]
for i in X.index:
    c = X.index.get_value(X,i)
    x.append(c)
print(x)

Y = (df2.loc[3]).astype(int)
y =[]
for i in Y.index:
    l = Y.index.get_value(Y,i)
    y.append(l)
print(y)

plt.plot(x,y,'ko')
plt.show()

#new_sample_df = df2.loc[1]
#new_sample_df.plot()
#plt.show()

#for df in dfs:
#    print(df)
#    df.reset_index(inplace=True)
 #   print(df.head())

style.use('fivethirtyeight')

#df['УИК №1725'].plot()
#plt.legend()
#plt.show()