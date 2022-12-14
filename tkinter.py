'''
from tkinter import *
def tug_bos():
    sozlar.configure(text="Mening ismim Davronbek")
add = Tk()

sozlar = Label( text="Salom hammaga!", bg="blue", font = ("Bernard MT Condensed", 20), cursor='dot', underline=1)
sozlar.pack(side=BOTTOM)
tugma=Button(text='ok', font = ("Bernard MT Condensed", 25) , command = tug_bos)
tugma.pack(side=LEFT, fill=Y)

add.mainloop()
'''

'''
from tkinter import *

add = Tk()
soz = Label(text="Salom", font = 20)

soz.place(x=62, y=160)

button = Button(text="OK")

button.place(x=25, y=105)

add.mainloop()
'''

'''
from tkinter import *

app = Tk()

soz = Label(text="Salom")

soz.grid(row=0, column=0)

tugma=Button(text="OK")

tugma.grid(row=0, column=1)

app.mainloop()

'''


# kalkulyator dasturi

from tkinter import*

def ikkiSonYigindi():
    ason = int(kritish1.get())
    bson = int(kritish2.get())

    sum = ason + bson

    yigindi.configure(text=str(sum))

def ikkiSonAyir():
    ason = int(kritish1.get())
    bson = int(kritish2.get())

    sum = ason - bson

    yigindi.configure(text=str(sum))

def ikkiSonKopaytir():
    ason = int(kritish1.get())
    bson = int(kritish2.get())

    sum = ason * bson

    yigindi.configure(text=str(sum))

def ikkiSonBol():
    ason = int(kritish1.get())
    bson = int(kritish2.get())

    sum = ason / bson

    yigindi.configure(text=str(sum))


app = Tk()

yigindi = Label(text="Hisoblanmadi")

yigindi.grid(row = 2, column = 0)

button1 = Button(text="Qo'sh", command = ikkiSonYigindi)
button2 = Button(text="Ayir", command = ikkiSonAyir)
button3 = Button(text="Ko'paytir", command = ikkiSonKopaytir)
button4 = Button(text="Bo'l", command = ikkiSonBol)

button1.grid(row = 0, column = 1)

button2.grid(row = 1, column = 1)

button3.grid(row = 2, column = 1)

button4.grid(row = 3, column = 1)

kritish1=Entry()
kritish1.grid(row = 0, column= 0)

kritish2=Entry()
kritish2.grid(row = 1, column= 0)


app.mainloop()







