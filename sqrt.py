import random as r
#son=[100, 200, 300, 400, 500]
#sonlar = list(map(sqrt, son))
#print(sonlar)
sonlar = r.sample(range(100), 10)
#print(sonlar)
def juftmi(x):
    return x%2==0
#juft_son=list(filter(juftmi, sonlar))
#print(juft_son)
#juft_son = list(filter(lambda x : x%2==0, sonlar ))
#print(juft_son)
mevalar = ['olma', 'anor', 'shaftoli', "o'rik"]
harf='a'
mevalar_a=list(filter(lambda meva : meva.startswith(harf), mevalar))
#print(mevalar_a)
mevalar2=list(filter(lambda meva:len(meva)<=5, mevalar ))
#print(mevalar2)
meva3=list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar))
print(meva3)
