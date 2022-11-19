
import random

def son_top(x=10):
    
    tasodifiy_son=random.randint(1, x)
    print(f"Men 1dan {x} gacha son o'yladim, topa olasizma")
    taxminlar=0
    while True:
        taxminlar+=1
        taxmin = int(input(">>>"))
        
        if taxmin < tasodifiy_son:
            print("Topolmadingiz men kattaroq son o'ylagan edim")
        elif taxmin > tasodifiy_son:
            print("Topolmadingiz men kichikroq son o'ylagan edim")
        else:
            break
            
    print("Topdingiz tabriklayman")
    print(f"siz {taxminlar} urunishda topdingiz")

def son_top_cs(x=10):
    
    input(f"Endi siz 1dan {x}gacha son o'ylang, men topaman")
    quyi=1
    yuqori=x
    taxminlar = 0
    
    while True:
        taxminlar+=1
        if quyi!=yuqori:
            tasodifiy_son = random.randint(1, x)
        else:
            tasodifiy_son=quyi
            
        javob=input(f"Siz o'ylagan son {tasodifiy_son}. kichik tanlasam'+', katta son tanlasam '-' \nto'g'ri bo'lsa 't' belgisini yozing".lower())

        if javob=='-':
            yuqori=tasodifiy_son-1
        elif javob == '+':
            quyi=tasodifiy_son+1
        else:
            break
    
    print(f"{taxminlar} urunishda topdim")
    return taxminlar
def play(x=10):
    yana = True
    while yana:
        taxminlar_user=son_top(x)
        taxminlar_cs=son_top_cs(x)
        if taxminlar_user > taxminlar_cs:
            print("Siz yutdingiz")
        elif taxminlar_user < taxminlar_cs:
            print("Men yutdim")
        else:
            print("Durrang")
        yana = int(input("Yana o'ynaysizma? '1' yoki '0' "))
    
        
    
