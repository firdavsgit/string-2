list =  [   "###",
            "###",
            "###"
]
result = 0
def character(lst,res):
    for x in lst:
        res += len(x)
    return res


print(character(list,result))