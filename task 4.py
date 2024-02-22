string = "eDaBiT"
result =[]
def index(str,res):
    for word in str:
        if word == word.upper():
            res.append(str.index(word))
    return res
print(index(string,result))