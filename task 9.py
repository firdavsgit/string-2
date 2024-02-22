

def vow(word,vowel,string):
    for x in word:
        if x not in vowel:
            string = string + x
    print(string)
vow("I have never seen a thin person drinking Diet Coke.","aioeu","")