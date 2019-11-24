import bs4 as bs
import pandas as pd
import geopandas as gpd
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
<<<<<<< HEAD
#print(df)
=======
print(df)
>>>>>>> 25d69e424016204dac9ab9b58af2e3e99d3ef34d

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
<<<<<<< HEAD
#print(y)
=======
print(y)
>>>>>>> 25d69e424016204dac9ab9b58af2e3e99d3ef34d

#Строим график зависимости явки от количества избирателей на участке;
fig1 = plt.figure()
plt.plot(x, y, 'b.')
plt.title('Явка от количества избирателей')
plt.xlabel('Число избирателей')
plt.ylabel('Процент явки')
plt.grid(color='b', linestyle=':', linewidth=0.5)
<<<<<<< HEAD
#plt.show()
=======
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
>>>>>>> 25d69e424016204dac9ab9b58af2e3e99d3ef34d

#Получаем список количества УИКов для каждого процента явки
t =[]
for i in range(100):
    z = 0
    for j in range(len(y)):
        if y[j] == i:
            z = z + 1
    t.append(z)
#print(t)

#Строим график зависимости явки от количества УИКов;
fig2 = plt.figure()
plt.plot(range(100), t, 'g-')
plt.title('Явка от количества УИКов')
plt.xlabel('Процент явки')
plt.ylabel('Число УИКов')
plt.grid(color='b', linestyle=':', linewidth=0.5)
#plt.show()

#------------------------       ВИЗУАЛИЗАЦИЯ НА КАРТЕ       ---------------------------#

my_district = gpd.read_file('/home/severin/Voting_SPB/Shape/border_level8_polygon.shp', encoding='utf-8')
#my_district = my_district.drop(my_district.index[[0,1,2,3,4,5,6,7]])
my_district = my_district.drop(['url', 'addr_count', 'admin_leve', 'addr_regio', 'boundary', 'wikidata', 'official_s', 'wikipedia', 'oktmo_user', 'oktmo', 'website', 'ref', 'name_en', "name_ru", 'place', 'old_name'], axis=1)
my_district.plot(column='name', linewidth=0.5, cmap='plasma', legend=True, figsize=[15, 15])

my_district = pd.DataFrame(my_district)
my_district.index = [0, 1, 2, 3, 4, 5, 6, 7]
mo_list = []

#with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
print(my_district)
''''
def mo_data(name):
    stat = [0] * 5
    for i in range(len(name)):
        if name[i] in tik11['№ УИК'].values:
            row = tik11[tik11['№ УИК'] == name[i]].index[0]
            stat[0] += tik11.iloc[row, 1]
            stat[1] += tik11.iloc[row, 3] + tik11.iloc[row, 4]
            stat[2] += tik11.iloc[row, 12]
            stat[3] += tik11.iloc[row, 13]
            stat[4] += tik11.iloc[row, 14]
        elif name[i] in tik17['№ УИК'].values:
            row = tik17[tik17['№ УИК'] == name[i]].index[0]
            stat[0] += tik17.iloc[row, 1]
            stat[1] += tik17.iloc[row, 3] + tik17.iloc[row, 4]
            stat[2] += tik17.iloc[row, 12]
            stat[3] += tik17.iloc[row, 13]
            stat[4] += tik17.iloc[row, 14]
    mo_list.append(stat)


mo_data(finland)
mo_data(u_21)
mo_data(akadem)
mo_data(grazhdan)
mo_data(piskar)
mo_data(sever)
mo_data(prometey)

mo_frame = pd.DataFrame(mo_list)
mo_frame.columns = ['kol-vo vsego', 'prishlo', 'Amosov', 'Beglov', 'Tihonova']
mo_frame['Amosov,%'] = mo_frame['Amosov'] / mo_frame['prishlo'] * 100
mo_frame['Beglov,%'] = mo_frame['Beglov'] / mo_frame['prishlo'] * 100
mo_frame['Tihonova,%'] = mo_frame['Tihonova'] / mo_frame['prishlo'] * 100
mo_frame['yavka'] = mo_frame['prishlo'] / mo_frame['kol-vo vsego'] * 100
mo_frame['winner'] = mo_frame.iloc[:, 3:5].idxmax(axis=1)

mo_frame['name'] = my_district['name']
mo_frame['geometry'] = my_district['geometry']
mo_frame = gpd.GeoDataFrame(mo_frame)

mo_frame.plot(column='winner', linewidth=2, cmap='plasma', legend=True, figsize=[10, 10])
mo_frame.plot(column='yavka', linewidth=2, cmap='BuPu', legend=True, figsize=[20, 20])
mo_frame.plot(column='Beglov,%', linewidth=2, cmap='YlOrRd', legend=True, figsize=[20, 20])
'''
