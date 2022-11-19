# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 12:23:06 2022

@author: User
"""
'''
narxlar=[8, 5, 9, 12, 45, 55]
qimmat=max(narxlar)
arzon=min(narxlar)
summa=sum(narxlar)
print(f"eng qimmat narx {qimmat}, eng arzon narx esa {arzon}, yig'indisi esa {summa}")

# ro'yxatni kesish

sav=['sabzi', 'kartoshka', 'piyoz', 'karam']
sav_k=sav[0:3]
print(sav_k)
cav=sav[:2]
print(cav)
'''
#ro'yxatdan nusxa olish
'''
sonlar=[8, 5, 9, 12, 45, 55]
sonlar2=sonlar[:]
sonlar2.append(18)
sonlar2.append(52)
print(sonlar)
print(sonlar2)

#typle() bu constanta

sonlar=(5, 6, 8, -7, 3)
print(sonlar)
sonlar=list(tuple(sonlar))
sonlar.append(66)
sonlar.append(54)
sonlar.remove(6)
print(tuple(sonlar))

davlatlar=['O\'zbekiston', 'Rossiya', 'AQSH', 'Yaponiya']
print(davlatlar)
print(len(davlatlar))
print(sorted(davlatlar))
print(davlatlar)
davlatlar.reverse()
print(davlatlar)
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)
sonlar5=list(range(120,1200,2))
print(sonlar5)

sonlar=[7, 9, 55, 21, 75]
summa=sum(sonlar)
print(summa)
minimal=min(sonlar)
maxsimal=max(sonlar)
print(maxsimal-minimal)
print(len(sonlar))

son=list(range(0, 200))
con=son[0:20]
son3=son[90:110]
son4=son[180:200]
print(con)
print(son3)
print(son4)
'''
taomlar=[]
taomlar.append('manti')
taomlar.append('sho\'rva')
taomlar.append('chuchvara')
taomlar.append('osh')
#print(taomlar)
nonushta=taomlar[:]
#print(nonushta)

nonushta.remove('manti')
nonushta.remove("sho'rva")
nonushta.append('qaymoq')
nonushta[0]="non va qaymoq"
print(tuple(nonushta))
print(taomlar)
