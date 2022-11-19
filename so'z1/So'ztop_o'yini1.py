# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 11:06:34 2022

@author: User
"""
import random
from uzwords import words

def get_word():
    word = random.choice(words)
    while "_" in word or ' ' in word:
        word = random.choice(words)
        return word.upper()
def displey(user_letters, word):
    displey_letter = " "
    for letter in word:
        if letter in user_letters:
            displey_letter += letter
        else:
            displey_letter += "_"
        return displey_letter
def play():
    word = get_word
    word_letter = set(word)
    user_letters = ''
    print(f"Men {len(word)} xonali son o'yladim, topingchi? ")
    while len(word_letter)>0:
        print(displey(user_letters, word))
        if len(word_letter)>0:
            print(f"Shuncha payitdan beri kiritgan hariflaringiz {user_letters}")
            
            letter = input("Harf kiriting: ").upper()
            if letter in user_letters:
                print("Bu harifni avval kiritgansiz, boshqa kiriting: ")
                continue
            elif letter in word:
                word_letter.remove(letter)
                print(f"{letter} harfi to'g'ri")
            else: 
                print("Bunday harf yo'q.")
            user_letters += letter
            print(f"Tabriklaymiz {word} so'zini {len(user_letters)} urinishda topdingiz. ")
            
