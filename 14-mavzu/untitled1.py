# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 19:52:19 2022
Dasturchi Davronbek Yo'ldoshev
@author: User
"""

#14-mavzu Nesting

car_0={
       'rusumi':'lasetti',
       'rangi':'oq',
       'chyil':2015,
       'narxi':10000,
       'km':500,
       'karobka':'mexanik'
       }
car_1={
       'rusumi':'nexia 3',
       'rangi':'qora',
       'chyil':2018,
       'narxi':12000,
       'km':1000,
       'karobka':'avtomat'
       }
car_2={
       'rusumi':"gentra",
       'rangi':'oq',
       'chyil':2020,
       'narxi':13000,
       'km':1000,
       'karobka':'avtomat'
       }
#cars=[car_0, car_1, car_2]
#print(cars)
'''
car=car_0
print(f"{car['rusumi'].title()},\
{car['rangi']} rangda,\
{car['chyil']}-yilda chiqqan,\
narxi {car['narxi']}$")

car=car_1
print(f"{car['rusumi'].title()},\
{car['rangi']} rangda,\
{car['chyil']}-yilda chiqqan,\
narxi {car['narxi']}$")

car=car_2
print(f"{car['rusumi'].title()},\
{car['rangi']} rangda,\
{car['chyil']}-yil chiqqan,\
narxi {car['narxi']}$")'''
'''
cars=[car_0, car_1, car_2]
for car in cars:
    print(f"{car['rusumi'].title()}, "
          f"{car['rangi']} rangda, "
          f"{car['narxi']}$")'''

#index bo'yicha murojaat qilish

#cars=[car_0, car_1, car_2]
#print(cars[0]['rangi'])
#print(cars[2]['chyil'])
#print(f"{cars[1]['rangi']} "
#f"{cars[2]['rusumi']}")
'''
gentraes=[]
for m in range(10):
   new_gentra={
        'rangi':None,
        'yili':2022,
        'narxi':None,
        'km':0,
        'karobka':'avtomat'
        }
   gentraes.append(new_gentra)
   
for gentra in gentraes[:3]:
    gentra['rangi']='qora'
    gentra['karobka']='mexanik'
   # print(gentra)
for gentra in gentraes[3:6]:
    gentra['rangi']='qizil'
    #print(gentra)
for gentra in gentraes[6:10]:
    gentra['rangi']='oq'
    #print(gentra)

for gentra in gentraes:
    if gentra['karobka']=='mexanik':
        gentra['narxi']='1000$'
    else:
        gentra['narxi']='1300$'
    print(gentra)'''
'''    
dasturchilar={
    'ali':['c++','python'],
    'vali':['python', 'sql'],
    'davron':['html', 'css', 'js'],
    'hasan':['c++','c#']
    }
for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi ", end='')
    for til in tillar:
        print(f"{til.upper()} ", end='')
        
hamkasblar={
    'ali':{'familya':'valiyev', 'yosh':19, 'dtil':['python', 'c++']},
    'vali':{'familya':'aliyev', 'yosh':19, 'dtil':['c', 'c++','c#']},
    'davron':{'familya':"yo'ldoshev", 'yosh':19, 'dtil':['python', 'sql']},
    }

for ism, info in hamkasblar.items():
    print(f"{ism.title()} {info['familya'].title()}, {info['yosh']} yoshda ")
    print('Quyidagi dasturlash tillarini biladi ')
    for til in info['dtil']:
        print(f"{til.upper()}")
       
allomalar={
    'Amir':{'familya':'Temur', 'tjoy':'Qashqadaryo Viloyati',\
'tyil':1336,'umri':69,'asarlari':['Temur Tuzuklari', 'Temuriylar']},
    'Alisher':{'familya':'Navoiy', 'tjoy':'Hirot', 'tyil':1441,'umri':60,\
'asarlari':['Hamsa', 'Lisson ut-tayir']},
    'Bobur':{'familya':'Mirzo', 'tjoy':'Andijon Viloyati', 'tyil':1483,'umri':47,\
'asarlari':['Boburnoma', 'Hind jangi']},
    'Abdulla':{'familya':'Qodiriy', 'tjoy':'Toshkent Viloyati', 'tyil':1915,'umri':40,\
'asarlari':["Otkan kunlar", 'Mehrobdan chayon']}
    }
for ism,info in allomalar.items():
    print(f"{ism.title()} {info['familya'].title()}, {info['tjoy']}da {info['tyil']}-yilda tug'ilgan, ",
f"{info['umri']} yil umr ko'rgan")
    print('Yozgan asarlari')
    for asar in info['asarlari']:
        print(f"{asar.upper()}")

kinolar={
    'ali':['Jekson', 'simba','jasorat'],
    'vali':["o'qdan tez",'Jasur','saraton'],
    'davron':['susanbil', 'jungli', 'rimbo']
    }
for ism, kino in kinolar.items():
    print(f"{ism.title()}ning sevimli kinolari ")
    print(f"{kino}")'''
    
davlatlar={
    "O'zbekiston":{'poytaxt':'Toshkent', 'aholi':33_000_000, 'maydoni':429_000},
    'Rossiya':{'poytaxt':'Moskva','aholi':124_000_000,'maydoni':17_000_000},
    'AQSh':{'poytaxt':'Vashington', 'aholi':240_000_000, 'maydoni':12_000_000}
    }
davlat=input("Sizga qaysi davlat haqida ma'lumot kerak? ")
if davlat in davlatlar:
    malumot=davlatlar[davlat]
    print(f"{davlat}ning poytaxti {malumot['poytaxt']}, "
f"aholisi {malumot['aholi']}, maydoni {malumot['maydoni']}km.kv")
else:
    print('Bizda bunday malumot yuq ')
   