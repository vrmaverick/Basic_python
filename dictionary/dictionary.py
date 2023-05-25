myDict = {
    "python":"a programming language",
    "keys":"value",
    "collection":[1,2,3,4,5],
    "nested dict": {"vedant":26,"op":79}
}
print(myDict['keys'])
print(myDict['python'])
print(myDict['collection'])
print(myDict['nested dict'])
print(myDict['nested dict']["vedant"])
print("**********************************************************************")
marks ={
    'vedant':91,
    'om':88,
    'niraker':90
}
print(marks['vedant'])
marks['vedant']=100
print(marks['vedant'])

# ..............................................................................................................
m_li = [
    {
        'a':[1,2,3],
        'b': True,
        'c':"STring"
    },
     {
        'a': [4,5,6],
        'b':True,
        'c':"STring"
    }
]
print(m_li[1]['a'][2])

d={
        '10': [4,5,6],
        10:True,
        True:"STring"
    }
print(d['10'])
print(d[10])
print(d[True])

