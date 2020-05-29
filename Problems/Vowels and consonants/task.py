vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
text = input()
length = len(text)
for i in range(0, length):
    if text[i] in vowels:
        print("vowel")
    elif text[i] in consonants:
        print("consonant")
    else:
        break
