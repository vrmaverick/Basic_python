import re
pattern = re.compile(r'[a-zA-Z].([v])')
fullmat = re. compile('VEDANT: Hi my name is vedant I hope you are having a great day')
string = 'VEDANT: Hi my name is vedant I hope you are having a great day'
print(pattern.search(string))
print(pattern.findall(string))
print(fullmat.fullmatch(string)) #for full match it should be same string