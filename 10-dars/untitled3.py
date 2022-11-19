# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 07:56:51 2022

@author: User
"""

#10-mavzu Bir nechta shartlar if-elif-else

# Dsturchi Yo'ldshev Dvaronbek
'''
narx=15000
non = False
choy=True
qahva=True
limonat=False
if non:
    print("xaridor non oldi")
    narx+=5000
if choy:
    print("xaridor choy oldi")
    narx+=5000
if qahva:
    print("xaridor qahva oldi")
    narx+=5000
if limonat:
    print("xaridor limonat oldi")
    narx+=5000
print(narx)

sonlar=[5, 6, 7, 12, -9]
7 in sonlar

ovqatlar=["osh", "manti", "sho'rva", "chuchvara"]
buyurtma=input("nima buyurtma qilasiz?\n>>>")
if buyurtma.lower() in ovqatlar:
    print("Buyurtma qabul qilindi.")
else:
    print("Afsuski bunday taom yo'q")
    
ovqatlar=["manti", "osh", "sho'rva", "chuchvara"]
buyurtma=input("nima buyurtma qilasiz?>>>")
if buyurtma.lower() not in ovqatlar:
    print("Afsuski bizda bunday taom yo'q")
else:
    print("Buyurtma qabul qilindi")'

ovqatlar=["osh", "manti", "lag'mon", "chuchvara", "kabob"]
buyurtma=["osh", "chuchvara", "qovun", "kabob", "somsa"]
if buyurtma:
    for taom in buyurtma:
        if taom in ovqatlar:
            print(f"menuda {taom} bor")
        else: 
            print(f"Afsuski, menuda {taom} yo'q")
else:
    print("ro'yxat bo'sh")
    
son=int(input("juft son kiriting: "))
if son%2==0:
    print("Raxmat!")
else:
    print("Bu juft son emasku?")

yosh=int(input("Yoshingiz nechida"))
if yosh < 4 or yosh > 60:
    print("Kirish bepul")
elif yosh<18:
    print("Kirish 10000 so'm")
else:
    print("Kirish 20000 so'm")
son1=int(input("Birinchi sonni kiriting"))
son2=int(input("Ikkinchi sonni kiriting"))
if son1==son2:
    print("teng")
elif son1>son2:
    print("Birinchi son katta")
else:
    print("Ikkinchi son katta")

mahsulotlar=["non", "kartoshka", "sabzi", "piyoz", "go'sht", "guruch", "qovun", "tarbuz", "handalak", "un"]
savat=[]
print("5 ta mahsulot kiriting")
for m in range(5):
    savat.append(input(f"Savatga {m+1}-mahsulotni qo'shing  "))
b_mah=[]
y_mah=[]
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        b_mah.append(mahsulot)
    else:
        y_mah.append(mahsulot)
if y_mah:
    print("Do'konimizda quyidagi mahsulotlar yo'q")
for mahsulot in y_mah:
    print(mahsulot)
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
    
mahsulolar=["non", "kartoshka", "sabzi", "piyoz", "go'sht", "qovin", "tarbuz", "shaftoli", "un"]
savat=[]
for n in range(5):
    savat.append(input(f"savat {n+1} -mahsulotni kiriting"))
for mahsulot in savat:
    if mahsulot in mahsulolar:
        print(f"Do'konimizda {mahsulot} bor")
    else: print(f"Do'konimizda {mahsulot} yo'q")
    
mahsulotlar=["non", "kartoshka", "sabzi", "piyoz", "go'sht", "qovin", "tarbuz", "shaftoli", "un"]
savat=[]
for n in range(5):
    savat.append(input(f"savatga {n+1}-mahsulotni qo'shing"))
b_mah=[]
y_mah=[]
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        b_mah.append(mahsulot)
    else: y_mah.append(mahsulot)
if y_mah:
    print("Do'konimiza quyidagi mahsulot(lar) yo'q")
for mahsulot in y_mah:
    print(mahsulot)
else:
    print("Do'konimizda barch mahsulotlar bor")
    
foydalanuvchilar=["anvar", "davron", "sanjar", "temur", "ozod"]
login=input("yangi login tanlang: ")
if login in foydalanuvchilar:
    print("login band")
else:
    print("xush kelibsiz")

son=int(input("istalgan butun sonni kiriitng: "))
for a in list(range(2,10)):
    if son%a==0:
        print(f"{son} {a} ga qoldiqsiz bo'linadi")'''
        
mahsulotlar=["non", "kartoshka", "sabzi", "piyoz", "go'sht", "qovin", "tarbuz", "shaftoli", "un"]
savat=[]
for n in range(5):
    savat.append(input(f"savatga {n+1}-mahsulotni qo'shing"))
bor_mahsulotlar=[]
yoq_mahsulotlar=[]
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
         yoq_mahsulotlar.append(mahsulot)
if yoq_mahsulotlar:
    print("quyidagi mahsulot(lar) yo'q")
for mahsulot in yoq_mahsulotlar:
        print(mahsulot)
else:
    print("Do'konimizda barcha mahsulotlar bor")
    
        
    
