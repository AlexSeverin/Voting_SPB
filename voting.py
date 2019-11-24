import bs4 as bs
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import datasets, linear_model
from matplotlib import style

#Список Территориальных избирательных комиссий
URL = 'http://www.st-petersburg.vybory.izbirkom.ru/region/region/st-petersburg?action=show&root=1&tvd=27820001217417&vrn=27820001217413&region=78&global=&sub_region=78&prver=0&pronetvd=null&vibid=27820001217417&type=222'

#Территориальные избирательные комиссии 9, 12, 28
URL9 = 'http://www.st-petersburg.vybory.izbirkom.ru/region/region/st-petersburg?action=show&tvd=27820001217417&vrn=27820001217413&region=78&global=&sub_region=78&prver=0&pronetvd=null&vibid=27820001217427&type=222'
URL12 = 'http://www.st-petersburg.vybory.izbirkom.ru/region/region/st-petersburg?action=show&tvd=27820001217417&vrn=27820001217413&region=78&global=&sub_region=78&prver=0&pronetvd=null&vibid=27820001217430&type=222'
URL28 = 'http://www.st-petersburg.vybory.izbirkom.ru/region/region/st-petersburg?action=show&tvd=27820001217417&vrn=27820001217413&region=78&global=&sub_region=78&prver=0&pronetvd=null&vibid=27820001217446&type=222'
#Получаем данные по Территориальная избирательным комиссиям 9, 12, 28
df9 = pd.read_html(URL9,header=0,encoding='cp1251')[7] #Территориальная избирательная комиссия 9
df12 = pd.read_html(URL12,header=0,encoding='cp1251')[7] #Территориальная избирательная комиссия 12
df28 = pd.read_html(URL28,header=0,encoding='cp1251')[7] #Территориальная избирательная комиссия 28

#Соединяем данные по Территориальным избирательным комиссиям 9, 12, 28 в одну общую таблицу (DataFrame)
df = df9.merge(df12, on=df9.index).iloc[:, 1:] #удаляем столбец key_0
df = df.merge(df28, on=df.index, how='outer').iloc[:, 1:] #удаляем столбец key_0
print(df)

#Функция преобразования строки DF в числовой список
def getint(datf):
    datf = (datf.astype(int))
    z=[]
    for i in datf.index:
        c = datf.index.get_value(datf,i)
        z.append(c)
    return(z)
#------------------------       ПОСТОЕНИЕ ГРАФИКОВ       ---------------------------#

x = getint(df.loc[0])   #Число избирателей всего на данном УИК
y = getint(df.loc[2])   #Число бюллетеней, выданных избирателям в помещении для голосования
y1 = getint(df.loc[3])  #Число бюллетеней, выданных избирателям вне помещения для голосования

#Получаем количество проголосовавших на каждом УИКе
for i in range(len(y1)):
    y1[i] = y[i] + y1[i]

#Получаем целый процент явки на каждом УИКе
for i in range(len(y)):
    y[i] = int((y1[i]/x[i])*100)
print(y)

#Строим график зависимости явки от количества избирателей на участке;
fig1 = plt.figure()
plt.plot(x, y, 'b.')
plt.title('Явка от количества избирателей')
plt.xlabel('Число избирателей')
plt.ylabel('Процент явки')
plt.grid(color='b', linestyle=':', linewidth=0.5)
plt.show()

#Получаем список количества УИКов для каждого процента явки
t =[]
for i in range(100):
    z = 0
    for j in range(len(y)):
        if y[j] == i:
            z = z + 1
    t.append(z)
print(t)

#Строим график зависимости явки от количества УИКов;
fig2 = plt.figure()
plt.plot(range(100), t, 'g-')
plt.title('Явка от количества УИКов')
plt.xlabel('Процент явки')
plt.ylabel('Число УИКов')
plt.grid(color='b', linestyle=':', linewidth=0.5)
plt.show()
import piptree
piptree install geopandas
#------------------------       ВИЗУАЛИЗАЦИЯ НА КАРТЕ       ---------------------------#
import geopandas as gpd
my_district = gpd.read_file('/Users/aleksejkozlov/Downloads/Kalininskiy/border_level8_polygon.shp', encoding='utf-8')

#y1 = getint(df.loc[11])   #Число бюллетеней, за Амосова на данном УИК
#dfA = list(map(int, df.loc[12].split()))
#print(dfA)


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