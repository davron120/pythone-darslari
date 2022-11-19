# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 20:07:45 2022

@author: User
"""

#8-dars FOR OPERATORI BILAN TANISHAMIZ
#dasturchi Davronbek Yo'ldoshev
'''
dostlar=["asad", "jabbor", "aziz", "jamshid"]
for dost in dostlar:
    # print(dost.title())
    print(f"hurmatli {dost.title()}bek, sizni 20-mart kuni Bo'riyevlar xonadoniga taklif etamiz Hurmat bilan Davronbek.")    
    print(dost)
    print(dostlar)

sonlar=list(range(1, 11))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng")
    
    
sonlar=list(range(11))
son_kv=[]
for son in sonlar:
    son_kv.append(son**2)    
print(sonlar)
print(son_kv)

dostlar=[]
print('istagan 5 ta do\'stingizni kiriting:')
for dost in range(5):
    dostlar.append(input(f"{dost+1}-do'stingizni kiriting: "))
print(dostlar)

dostlar=["asad", "jabbor", "aziz", "jamshid"]
for a in dostlar: 
    print(f"Salom {a}")
print(f"Kod {len(dostlar)} martta takrorlandi " )

sonlar=list(range(11, 100, 2))
for n in sonlar:
    print(n**3)
    
    
kinolar=[]
for n in range(5):
    kinolar.append(input(f"{n+1}-kinoni kiriting "))
print(kinolar)'''

son=int(input("Bugun nechi kishi bilan uchrashdingiz?>>>"))
ism=[]
for a in range(son):
    ism.append(input(f"{a+1}-suhbat qilgan odamingiz kim edi? "))
print(ism)