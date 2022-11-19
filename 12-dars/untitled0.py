#12-mavzu lug'at
#dasturchi Yo'ldoshev Davronbek
'''
otam={'ism':'saidakbar', 'yosh':'41', 't_joy':'surxandaryo'}
ism=otam['ism']
t_joy=otam['t_joy']
print(f"Otamning ismi {ism.title()},yoshi {otam['yosh']}da,\
tug'ilgan joyi {t_joy.title()}")'''
'''
taom={'Ali':'osh', 'Vali':'chuchvara','Ikrom':'shashlik',\
'Islom':'amnti','Davron':'kabob'}
print(f"Alining yaxshi ko'rgan taomi {taom['Ali']}")
print(f"Valining yaxshi ko'rgan taomi {taom['Vali']}")
print(f"Ikromning yaxshi ko'rgan taomi {taom['Ikrom']}")'''
'''
kalit=input("Biror kalit so'z kiriting")
python={'int':'butun son', 'float':'haqiyqiy son', 'if':'agar', 'else':'yoki',\
'string':'matn', 'char':'belgi', 'input':'kirgiz', 'print':'chiqar'}
if kalit in python:
    phone=python.get(f"{kalit}", 'bunday so\'z yo\'q')
print(phone)'''

kalit=input("Biror kalit so'z kiriting ")
python={'int':'butun son', 'float':'haqiyqiy son', 'if':'agar', 'else':'yoki',\
'string':'matn', 'char':'belgi', 'input':'kirgiz', 'print':'chiqar'}
if kalit in python:
    print(f"{kalit} so'zining ma'nosi {python[kalit]} ")
else:
    print("Bunday so'z yo'q")