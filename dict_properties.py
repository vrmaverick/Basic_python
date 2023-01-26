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







