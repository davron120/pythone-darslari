# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 09:05:52 2022

@author: User
"""
'''
#ishora orqali while()
print("Istalgan sonni kvadratini chiqaruvchi dastur")
savol="Istagan soningizni kiriting "
savol+=("agar dasturdan chiqishni xoxlasangiz 'exit' deb yozing ")
ishora=True
while ishora:
    print(' ')
    qiymat=input(savol)
    if qiymat == 'exit':
        ishora=False
    else:
        print(float(qiymat)**2)      
print('Dastur tugadi')

#break orqali while
print("Istalgan sonni kvadratini chiqaruvchi dastur")
savol="Istagan soningizni kiriting "
savol+=("agar dasturdan chiqishni xoxlasangiz 'exit' deb yozing ")

while True:
    qiymat=input(savol)
    if qiymat=='exit':
        break
    else:
        print(float(qiymat)**2)
print('Dastur tugadi')

sonlar = list(range(1,11))
for son in sonlar:
    if son==5:
        break
    else:
        print(f"{son}ning kvadrati {son**2}ga teng")
       
sonlar = list(range(1,11))
for son in sonlar:
    if son==5:
        continue
    else:
        print(f"{son}ning kvadrati {son**2}ga teng")
        
son=0
while son<10:
    son+=1
    if son%2!=0:
        continue
    else:
        print(son)

#abadiy sikl
son=0
while son<10:
    if son%2!=0:
        continue
    else:
        print(son)
#abadiy sikl    
son=0
while son<10:
    if son%2!=0:
        continue
    else:
        print(son)
        son+=1

son=1
while son>0:
    son+=1
    if son%2!=0:
        continue
    else:
        print(son)

kitob = "Yaxshi ko'rgan kitobingni kirit "
kitob+=" agar dasturdan chiqishni istasang 'stop' ni kirit"
soz=''
while soz!='stop':
    soz=input(kitob)
    if soz!='stop':
        print(soz)
    else:
        print('dastur tugadi')

muzey="Yoshingizni kiriting "
muzey+="agar dasturdan chiqishni hoxlasangiz 'exit' yoki 'quit' ni kriting "
while True:
    qiymat=input(muzey)
    if qiymat == 'exit' or qiymat == 'quit':
        break
    yosh=int(qiymat)
       # print('chipta narxi quyidagicha')
    if yosh<4:
        print("chipta 2000so'm ")
    elif yosh<18:
        print("chipta 8000 so'm")
    elif yosh < 65:
        print("chipta 20000 so'm ")
    elif yosh >65:
        print("chipta tekin")
print('dastur tugadi') 

muzey="Yoshingizni kiriting "
muzey+="agar dasturdan chiqishni hoxlasangiz 'exit' yoki 'quit' ni kriting "
ishora=True
while True:
    qiymat=input(muzey)
    if qiymat == 'exit' or qiymat == 'quit':
        ishora=False 
        break
    else:
        yosh=int(qiymat)
    if yosh<4:
        print("chipta 2000so'm ")
    elif yosh<18:
        print("chipta 8000 so'm")
    elif yosh < 65:
        print("chipta 20000 so'm ")
    elif yosh >65:
        print("chipta tekin")
print('dastur tugadi')'''

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    elif float(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
        
