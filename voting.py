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
'''
Приморский 
Территориальная
избирательная
комиссия №9
муниципальный округ Черная речка,
муниципальный округ Озеро Долгое
Территориальная
избирательная
комиссия №12
муниципальный округ Лахта-Ольгино,
муниципальный округ №65,
поселок Лисий Нос
Территориальная
избирательная
комиссия №28
муниципальный округ Комендантский
аэродром,
муниципальный округ Юнтолово,
муниципальный округ Коломяги
'''

import bs4 as bs
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import datasets, linear_model
from matplotlib import style

#Получаем данные по Территориальная избирательным комиссиям 9, 12, 28
URL9 = 'http://www.st-petersburg.vybory.izbirkom.ru/region/region/st-petersburg?action=show&tvd=27820001217417&vrn=27820001217413&region=78&global=&sub_region=78&prver=0&pronetvd=null&vibid=27820001217427&type=222'
URL12 = 'http://www.st-petersburg.vybory.izbirkom.ru/region/region/st-petersburg?action=show&tvd=27820001217417&vrn=27820001217413&region=78&global=&sub_region=78&prver=0&pronetvd=null&vibid=27820001217430&type=222'
URL28 = 'http://www.st-petersburg.vybory.izbirkom.ru/region/region/st-petersburg?action=show&tvd=27820001217417&vrn=27820001217413&region=78&global=&sub_region=78&prver=0&pronetvd=null&vibid=27820001217446&type=222'

df9 = pd.read_html(URL9,header=0,encoding='cp1251')[7] #Территориальная избирательная комиссия 9
df12 = pd.read_html(URL12,header=0,encoding='cp1251')[7] #Территориальная избирательная комиссия 12
df28 = pd.read_html(URL28,header=0,encoding='cp1251')[7] #Территориальная избирательная комиссия 28

#print(df9)
#print(df12)
#print(df28)
#Соединяем данные по Территориальная избирательным комиссиям 9, 12, 28 в одну общую таблицу
df = df9.merge(df12, on=df9.index).iloc[:, 1:] #удаляем столбец key_0
df = df.merge(df28, on=df.index, how='outer').iloc[:, 1:] #удаляем столбец key_0
#print(df)
#Функция преобразования строки DF в числовой вид
def getint(datf):
    datf = (datf.astype(int))
    z=[]
    for i in datf.index:
        c = datf.index.get_value(datf,i)
        z.append(c)
    return(z)

x = getint(df.loc[0])   #Число избирателей всего на данном УИК
y = getint(df.loc[2])   #Число бюллетеней, выданных избирателям на данном УИК
#y1 = getint(df.loc[11])   #Число бюллетеней, за Амосова на данном УИК
dfA = list(map(int, df.loc[12].split()))
print(dfA)

#вывод и Линейная аппроксимация полученных данных
def plot(x,y,label):
    x=np.array(x).reshape(-1,1)
    y=np.array(y).reshape(-1,1)
    l=LinearRegression().fit(x,y)
    c=l.coef_[0][0]
    xmin=min(x)
    xmax=max(x)
    ls=np.linspace(xmin,xmax)
    plt.title(label)
    plt.grid(color='b', linestyle=':', linewidth=0.5)
    plt.plot(ls,ls*c,color='red')
    plt.scatter(x,y)
    plt.legend(['МНК','Голоса'])
    #print('MSE =',mean_squared_error(y,x*c))
    #print('R2 score = ',r2_score(y,x*c))
    plt.show()
    #print()
#plot(x,y, 'Явка избирателей')

fig = plt.figure()
plt.plot(x, y, 'ko')
plt.title('Явка избирателей')
# Добавляем подписи к осям:
plt.xlabel('Число избирателей')
plt.ylabel('Число бюллетеней, выданных избирателям')
plt.xticks(range(min(x),max(x),250))
plt.yticks(range(min(y),max(y),250))
plt.grid(color='b', linestyle=':', linewidth=0.5)

#plt.show()
print(max(y))
''''
URL = 'http://www.st-petersburg.vybory.izbirkom.ru/region/region/st-petersburg?action=show&root=1&tvd=27820001217417&vrn=27820001217413&region=78&global=&sub_region=78&prver=0&pronetvd=null&vibid=27820001217417&type=222'

df1 = pd.read_html(URL,header=0,encoding='cp1251')[5].iloc[:, 1:].rename(columns={'Unnamed: 1':'Name'}) #Наименоване избирательной комиссии
print(df1)

df2 = pd.read_html(URL,encoding='cp1251')[7].iloc[:, 1:] #Территориальные избирательные комиссии с 1 по 30
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
'''
#new_sample_df = df2.loc[1]
#new_sample_df.plot()
#plt.show()

#for df in dfs:
#    print(df)
#    df.reset_index(inplace=True)
 #   print(df.head())

#df['УИК №1725'].plot()
#plt.legend()
#plt.show()