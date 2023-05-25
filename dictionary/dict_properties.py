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
print("###############################################")
print(myDict.keys())
print(type(myDict.keys()))
print("###############################################")
print(list(myDict.keys()))#dict keys converted to list
print("###############################################")
print(myDict.values())
print("###############################################")
print(myDict.items())
print("###############################################")
new = {
    "newitem":"adding",
    "collection":[68,69]
}
myDict.update(new)#new dict added to old dict
print(myDict)
print(myDict.get("collection"))#will return none if collection is not found in dictionary
# print(myDict["collection"])#will throw error if collection is not found as a key

d={
        '10': [4,5,6],
        10:True,
        True:"STring"
    }
print ("STring" in d)#...false by defualt checks only keys
print ("10" in d.keys())
print ("STring" in d.values())

# d2=d
# d.clear()
# print(d2) #empty

d3=d.copy()
d.clear()
print(d3)






