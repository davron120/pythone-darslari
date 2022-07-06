# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 07:46:16 2022

@author: User
"""

#13-mavzu. LUG'AT ELEMENTLARI BILAN ISHLASH
#Dasturchi Davronbek Yo'ldoshev

mahsulotlar={
    'olma':10000,
    'banan':15000,
    'sabzi':3000,
    'behi':4000,
    'anor':12000
    
    }
#for mahsulot in mahsulotlar.items():
 #   print(mahsulot)
 
#for k, q in mahsulotlar.items():
#     print(f"{k}ning narxi {q}so'm")
     
#for mahsulot in mahsulotlar.keys():
 #   print(mahsulot)
 
bozorlik={
    'olma':10000,
    'banan':15000,
    'xurmo':18000,
    'sabzi':3000,
    'karam':7000
    
    }
#for mahsulot in mahsulotlar:
 #   if mahsulot in bozorlik:
#        print(f"bozordan {mahsulot} oldim")
 #   else:
 #       print(f"bozorga {mahsulot}ni ham olib keing")
 
telifon={
    'ali':'core 2',
    'vali':'j2',
    'xamdam':'A10',
    'komil':'A20'
    }
#for tel in sorted(telifon.keys()): #kalitni saralaydi
#for tel in sorted(telifon.values()): #qiymatni saralash uchun
#    print(tel)
    
talaba_0={
    'ism':'davronbek',
    'yosh':19,
    'kurs':2,
    "yo'nalish":"dasturiyinjiniring",
    'familya':'davronbek'
    }
#print(talaba_0)

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'    
    }
#for tel in set(telefonlar.values()):
#    print(tel)

python={
        'int':'butun son',
        'float':'haqiyqiy son',
        'bool':'mantiqiy operator',
        'input()':'kiritish',
        'print()':'chiqarish'
        }
#for p in sorted(python.items()):
#    print(p)

dav_poy={
    "O'zbekiston": 'Toshkent',
    'Rossiya':'Maskva',
    "Qozog'iston":"Astana",
    'AQSh':'Vashington',
    'Singapur':'Singapur'
    }
#davlat=input("Qaysi davlatning poytaxtini bilishni xoxlaysiz:\n>>> ")

#if davlat in dav_poy:
 #       print(f"{davlat}ning poytaxti {dav_poy[davlat]}")
#else:
 #       print("Uzur, bizda bunday ma'lumot yo'q")

#print('Dunyo Davlatlari')
#for d in dav_poy:
 #   print(f"{d.upper()}")
#print(' ')
#print('Davlatlarning poytaxtlari')
#for p in dav_poy.values():
 #   print(p)
 
menyu={
       'osh':15000,
       'manti':20000,
       'somsa':8000,
       'shashlik':15000,
       "lag'mon":25000
       }
buyurtmalar=[]
print("3 ta taom buyurtma bering ")
for a in range(3):
    buyurtmalar.append(input(f"{a+1}-taom: ").lower())
for buyurtma in buyurtmalar:
    if buyurtma in menyu:
        print(f"{buyurtma.title()} {menyu[buyurtma]} so'm ")
    else:
        print(f"Kechirasiz bizda {buyurtma} yo'q")