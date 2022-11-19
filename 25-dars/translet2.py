from transliterate import to_cyrillic, to_latin

matin = input("Matin kiriting: ")
if matin.isascii():
    print(to_cyrillic(matin))
else:
    print(to_latin(matin))
