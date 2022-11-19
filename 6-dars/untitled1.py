# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 11:07:40 2022

@author: User
"""

#friendsnomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga
# chaqirmoqchi bo'lgan do'stlaringizni kiriting. 

frindes=[]
frindes.append('Asad')
frindes.append('Jabbor')
frindes.append('Ozodbek')
frindes.append('Sanjar')
print(f"{frindes} , barchalaringizni bugun mehmonga chaqiraman")
frindes.remove('Jabbor')
print(f"Mehmonga kelganlar ro'yxati: {frindes}")
frindes.insert(0,'Ali')
frindes.insert(3, 'Vali')
frindes.append('Komil')
print(frindes)
mehmonlar=[]
mehmonlar.append(frindes.pop(1))
mehmonlar.append(frindes.pop(0))
mehmonlar.append(frindes.pop(3))
print(mehmonlar)