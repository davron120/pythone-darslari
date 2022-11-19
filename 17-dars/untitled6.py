# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 10:06:06 2022
Dasturchi Davronbek Yo'ldoshev'
@author: User
"""
#17-mavzu Funksiya
"""
def salom_ber():
    '''salom beruvchi funksiya'''
    print("Assalomu alaykum")

salom_ber()


def salom_ber(ism):
    foydalanuvchi ismini qabul qilib oluvchi
va salom beruvchi funksiya
    print(f"Assalomu alaykum {ism.capitalize()}")

salom_ber('davronbek')
salom_ber('asad')

def toliq_ism(ism, familya):
    '''to'liq ism va familyani chiqaruvchi funksiya'''
    print(f"Foydalanuvchi ismi: {ism.capitalize()}\n"
          f"Foydalanuvchi familyasi: {familya.capitalize()}")
toliq_ism('davronbek', "yo'ldoshev")

def yoshini_aniqla(ism, t_yil):
    '''yoshini aniqlovchi funksiya'''
    print(f"{ism.title()}ning yoshi {2022-t_yil} da")

yoshini_aniqla('davronbek', 2003)

def toliq_ism(ism, familya):
    '''to'liq ism va familyani chiqaruvchi funksiya'''
    print(f"Foydalanuvchi ismi: {ism.capitalize()}\n"
          f"Foydalanuvchi familyasi: {familya.capitalize()}")
toliq_ism(familya="yo'ldoshev",ism='davronbek')

def yosh(t_yil, j_yil=2022):
    '''Foydalanuvchining tug'ilgan yiliga murojat qilib\n
    uning yoshini aniqlovchi funksiya'''
    print(f"Sizning yoshingiz {j_yil-t_yil} da")
yosh(2003, 2022)
yosh(2003)

def yosh(t_yil, j_yil=2022):
    '''Foydalanuvchining tug'ilgan yiliga murojat qilib\n
    uning yoshini aniqlovchi funksiya'''
    print(f"Sizning yoshingiz {j_yil-t_yil} da")
t_yil=int(input("Tug'ilgan yilingizni kiriting: "))
yosh(t_yil)

#Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan
# yilini hisoblaydigan funksiya yozing.
def t_yil(yosh, j_yil=2022 ):
    '''Foydalanuvchi ismi va yoshini so'rab, uning
    tug'ilgan yilini hisoblaydigan funksiya yozing.'''
    ism=input("ismingizni kiriting: ")
    yosh=int(input("yoshingizni kiriting: "))
    print(f"{ism.title()}ning tug'ilgan yili {j_yil-yosh}")

t_yil(19)

#Foydalanuvchidan son olib, uning kvadrati va kubini 
#konsolga chiqaruvchi funksiya yozing.

def son_kv(son):
    '''son olib, uning kvadrati va kubini 
    konsolga chiqaruvchi funksiya'''
    son=int(input("Istalgan sonni kiriting: "))
    print(f"{son}ning kvadrati {son**2}, kubi esa {son**3} ga teng")
son_kv(3)

#Foydalanuvchidan son olib, son juft yoki toqligini konsolga
# chiqaruvchi funksiya yozing.

def son_juft(son):
    '''son olib, son juft yoki toqligini konsolga
     chiqaruvchi funksiya'''
    son=int(input("istalgan sonni kiriting: "))
    if son % 2==0:
        print("juft")
    else:
        print("toq")
son_juft(6)

#Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga
# chiqaruvchi funksiya yozing. Agar sonlar teng bo'lsa
# "Sonlar teng" degan xabarni chiqaring.

def son_taqqosla(son):
    '''ikkita son olib, ulardan kattasini konsolga
    chiqaruvchi funksiya'''
    son1=int(input("1-sonni kiritng: "))
    son2=int(input("2-sonni kiriting: "))
    if son1>son2:
        print(son1)
    elif son1<son2:
        print(son2)
    else:
        print("sonlar teng")
son_taqqosla(7)"""
#Foydalanuvchidan x va y sonlarini olib, ni konsolga
# chiqaruvchi funksiya yozing.

def son_kv(x,y):
    '''x va y sonlarini olib, ni konsolga
     chiqaruvchi funksiya'''
     x=int(input("1-sonni kiriting: "))
     y=int(input("2-sonni kiriting: "))
     print(x**y)
son_kv(6, 3)