'''
talaba_0 = {"Ism" : "Davronbek", 
            "Familyasi":"Yo'ldoshev", 
            "Yoshi":19, 
            "Fakultet":"Dasturiy injiniring", 
            "Kursi":2}

for kalit, qiymat in talaba_0.items():
    
  print(f"Kalit: {kalit} ")
  print(f"Qiymat {qiymat} \n")
  
  
mahsulotlar = {"olma":5000,
               "anor":10000,
               "non":3000,
               "sut":5000,
               "shokalat":10000,
               "novot":23000}
retsep = {
    "anor":10000,
    "sut":5000,
    "snikrs":15000,
    "un":260000,
    "asal":80000}
print([mahsulotlar])
for mahsulot in mahsulotlar:
    if mahsulot in retsep:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")


cars=[]

for car in range(10):
    car_0={"rusumi":"malibu",
        "rangi":"qora",
        "narxi":None,
        "yili":2022,
        "karobka":"avto"}
    cars.append(car_0)
#for malibu in cars:
#    print(malibu)

for malibu in cars[:3]:
    malibu['rangi']="qizil"

for malibu in cars[3:6]:
    malibu['rangi']="oq"

for malibu in cars[6:]:
    malibu['rangi']="sariq"
    malibu['karobka']="mexanik"
    
    
for malibu in cars:
    if malibu['karobka']=="avto":
        malibu['narxi']=40000
    else:
        malibu['narxi']=35000
        
for malibu in cars:
    print(malibu)


dasturchilar = {
    "Ali":["c++", "python"],
    "Vali":["java", "C#"],
    "Husan":["python", "javaskript"],
    "Hasan":["c++", "C#"]
    }
for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi adsturlash tillarini biladi")
    for til in tillar:
        print(til.upper())

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi adsturlash tillarini biladi")
    for til in tillar:
        print(f'{til.upper()}', end='')'''
        
        
'''
savol = "Istalgan sonno kiriting"
savol += "Agar kiritgan qiymatingiz 'exit' bo'lsa dastur tugaydi"
qiymat=''
while qiymat != 'exit':
    qiymat=input(savol)
    if qiymat != 'exit':
        print(float(qiymat**2))
print("dastur tugadi")

print("Yaqin do'stlaringiz ro'yxatini kiriting:")
ismlar=[]
n=1
while True:
      Savol=f"{n} - do'stingizni ismini kiriting "
      ism=input(Savol)
      ismlar.append(ism)
      takrorla=input("Yana do'stlaringizni kiritasizma(ha/yo'q)")
      n+=1
      if takrorla!='ha':
          break
print("Sizning do'stlaringiz ro'yxati:")
for ism in ismlar:
    print(ism)
'''
'''
dostlar={}
ishora=True
while ishora:
    ism=input("Do'stingizning ismini kiriting: ")
    yosh=input(f"{ism.title()}ning yoshi: ")
    dostlar[ism]=int(yosh)
    takrorla=input("Yana do'stingizni ismini kiritasizma(ha/yo'q)")
    if takrorla !='ha':
        ishora=False
for ism, yosh in dostlar.items():
    print(f"{ism.title()}ning yoshi {yosh}da")
  '''
'''
cars=['lasetti', 'spark', 'nexia', 'cobalt', 'nexia', 'jentra']
while 'nexia' in cars:
    cars.remove('nexia')
print(cars)
'''
'''
talabalar = ['nodir', 'sobir', 'jahon', 'olim']
talaba_baho={}
while talabalar:
    talaba=talabalar.pop()
    baho=input(f"{talaba.title()}ni bahosini qo'ying")
    print(f"{talaba.title()} baholandi")
    talaba_baho[talaba]=baho
    '''
'''  
def salom_ber(ism):
    print(f"Assalomu alaykum xurmatli {ism.title()}")
salom_ber('davron')
salom_ber('jahon')
'''
'''
def toliq_ism_yasa(ism, familya):
    toliq_ism=f"{ism.title()} {familya.title()}"
    return toliq_ism
talaba = toliq_ism_yasa("davron", "yo'ldoshev")
print(talaba)
'''
'''
def toliq_ism_yasa(ism, familya):
    toliq_ism=f"{ism.title()} {familya.title()}"
    return toliq_ism
talaba1 = toliq_ism_yasa("davron", "yo'ldoshev")
talaba2 = toliq_ism_yasa("jahon","davronov")
print(f"Bugun darsga {talaba1} va {talaba2} talabalar keldi")
'''
'''
def toliq_ism_yasa(ism, familya, otasining_ismi=''):
    if otasining_ismi:
        toliq_ism=f"{ism.title()} {otasining_ismi.title()} {familya.title()}"
    else: toliq_ism=f"{ism.title()} {familya.title()}"
    return toliq_ism
talaba1 = toliq_ism_yasa("davron", "yo'ldoshev")
talaba2 = toliq_ism_yasa("jahon", "davronov", "Saidazimovich")
print(f"Bugun darsga quyidagi talabalar kelmadi:{talaba1}, {talaba2}")
'''
'''
def avto_info(kompaaniya, model, rang, narx=None):
    avto = {
        'kompaniya':kompaaniya,
        'model': model,
        'rang':rang,
        'narx':narx
        
        }
    return avto
avto1=avto_info("gm", "malibu", "qora")
avto2=avto_info("gm", "cobalt", "oq", "105000")
avtolar=[avto1, avto2]
print("Online bozordagi mavjud mashinalar")
for avto in avtolar:
    if avto['narx']:
        narx=avto['narx']
    else:
        narx="No'malum"
    print(f"{avto['rang']} {avto['model']} Narxi:{narx}")
    
def oraliq(min, max, qadam):
    sonlar=[]
    while min<max:
        sonlar.append(min)
        if qadam<max:
            min+=qadam
        else: 
            min+=1
    return sonlar
print(oraliq(0, 10, 2))
print(oraliq(20, 30))
'''
'''
def avto_info(kompaaniya, model, rang, narx=None):
    avto = {
        'kompaniya':kompaaniya,
        'model': model,
        'rang':rang,
        'narx':narx
        }
    return avto

print("Saytimizdagi avtolar ro'yxatini shakillantiramiz")
avtolar=[]
while True:
    print("\nQuyidagi ma'lumotlarni kiriting" )
    kompaaniya=input("Kompaniya: ")
    model=input("Modeli: ")
    rang=input("Rangi: ")
    narx=input("narxi: ")

    avtolar.append(avto_info(kompaaniya, model, rang, narx))
    javob=input("Yana avtomabil qo'shasizma(no/yes) ")
    if javob=='no':
        break
print("\nSaytimizdagi avtomabillar")
for avto in avtolar:
    if avto['narx']:
        narx=avto['narx']
    else: narx="Nomalum"
    print(f"{avto['rang'].title()} {avto['model'].title()}, Narx: {narx}")
    
  
  
def bahola(ismlar):
    baholar={}
    while ismlar:
        ism=ismlar.pop()
        baho=input(f"{ism.title()}ning bahosi: ")
        baholar[ism]=int(baho)
    return baholar
talabalar = ['ali', 'vali', 'ilhom', 'mansur']
baholar=bahola(talabalar)
print(baholar)
    
  
def summa(*sonlar):
    return sum(sonlar)
print(summa(1, 2))
print(summa(5, 4, 3, 2, 1))
print(summa(4, 8, 9, 10))


def summa(x, y, *sonlar):
    return x+y+sum(sonlar)
print(summa(1, 2))
print(summa(5, 4, 3, 2, 1))
print(summa(4, 5, 6, 8))
'''
'''
def avto_info(kompaniya, model, **malumot):
    
        malumot['kompaniya']=kompaniya
        malumot['model']= model
        return malumot
print(avto_info('gm', 'jentra', rangi="oq", karobka='avtomat'))
print(avto_info('gm', 'cobalt', rangi='qora', karobka='avtomat', narxi=13000))


file = open("davron.txt")
PI=file.read()
print(PI)
file.close()
'''
'''
class Talaba:
    def __init__(self, ism, familya, tyil):
        self.ism=ism
        self.familya=familya
        self.tyil=tyil
    def tanishtir(self):
        print(f"Ismim {self.ism} {self.familya}, tug'ilgan yilim {self.tyil}-yil")
talaba1=Talaba("Olim", "Asadov", 2000)
talaba2=Talaba("Shoxrux", "Saidov", 2003)
talaba3=Talaba("Davron", "Yo'ldoshev", 2003)




class tortburchak:
    def __init__(self, width, height):
        self.width=width  
        self.height=height
    def tanishtir(self):
        print(f"To'rtburchakning eni {self.width}, bo'yi {self.height}")
t1=tortburchak( 30, 50)
t2=tortburchak( 20, 40)
'''


#ismlar=["Asad", "Davronbek", "Ozodbek", "Shamish", "Qamar"]
#ism=r.choice(ismlar)
#print(ism)
#print(r.choice(ism))


#son=list(range(0, 51, 5))
#print(son)
#print(r.choice(son))
'''
son = list(range(11))
print(son)
r.shuffle(son)
print(son)


import math as m
son=m.sqrt(625)
son1=m.pow(5, 3)
print(son1)
print(son)
son3=m.pi
print(son3)

'''
import random as ra
print(ra.PI)













