word = "hello world"
word2 = ""
def repit(w,w2):
    for x in w:
        w2 = w2 + x*2
    return w2
print(repit(word,word2))
