# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 19:29:55 2022

@author: User
"""
'''
print("Yaqin do'stlaringizning ro'yxatini tuzamiz ")
ismlar=[]
n=1
while True:
    savol=f"{n}-do'stingizni kiriting: "
    ism=input(savol)
    ismlar.append(ism)
    takrorlash=input("Yana do'stlaringizni qo'shasizma(ha/yo'q)?")
    n+=1
    if takrorlash != 'ha':
        break
print("Yaqin do'stlaringizning ro'yxati")
for ism in ismlar:
    print(ism.title())

print("Yaqin do'stlaringiz yoshini saqlaymiz")
dostlar={}
ishora=True
while True:
    ism=input("Ismingizni kiriting: ")
    yosh=input(f"{ism.title()}ning yoshi nechida? ")
    dostlar[ism]=int(yosh)
    
    takrorlash=input("Yana do'stlaringizni qo'shasizma?(ha/yo'q)")
    if takrorlash == "yo'q":
        ishora=False
        break

for ism, yosh in dostlar.items():
    print(f"{ism.title()}ning yoshi {yosh} ga teng")'''
    
cars=['lasetti', 'nexia', 'cobalt', 'gentra', 'nexia', 'spark', 'nexia']
#while 'nexia' in cars:
#    cars.remove('nexia')
#print(cars)

#while 'nexia' in cars:
   # del cars[3]
 #   cars.remove('nexia')
#print(cars)
'''
talabalar=['botir', 'sobir', 'hasan', 'husan']
baholangan_talabalar={}
while talabalar:
    print('')
    talaba=talabalar.pop()
    baho=int(input(f" {talaba.title()} ning bahosini qo'ying: "))
    print(f"{talaba.title()} baholandi. ")
    baholangan_talabalar[talaba]=int(baho)
print(baholangan_talabalar)

print("Do'stlarimning ismlarining ro'yxati")
ismlar=[]
n=1
while True:
    ism=input(f"{n}-do'stingizning ismini kiriting: ")
    ismlar.append(ism)
    takrorlash=input("Yana do'stlaringizni qo'shasizma(ha/yo'q)?")
    n+=1
    if takrorlash != 'ha':
        break
print(ismlar)

mahsulotlar={}

while True:
    savol1=input("Sizga qanday mahsulot kerak? ")
    savol2=int(input("Bu mahsulotdan necha so'mlik kerak? "))
    mahsulotlar[savol1]=savol2
    takrorlash=input("Yana mahsulot kerakmi(ha/yo'q')")
    if takrorlash != 'ha':
        break
print(mahsulotlar)
savat=[]
n=1
while True:
        savat.append(input("Sizga qanday mahsulot kerak? "))
        takrorlash=input("Yana mahsulot qo'shmoqchimisiz?(ha/yo'q)")
        if takrorlash != 'ha':
            break
print(savat)

for savol1, savol2 in mahsulotlar.items():    
    if mahsulotlar in savat:
        print(mahsulotlar.keys())'''
buyurtmalar=['non', 'choy', 'shakar', 'un', "o'rik"]
mahsulotlar={
    'non':18000,
    'un':230000,
    "yog'":115000,
    "shakar":6000,
    "kartoshka":5000,
    "sabzi":3000
    }

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar:
        narx = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()}-{narx} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")