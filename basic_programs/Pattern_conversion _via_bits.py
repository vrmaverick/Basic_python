picture = [
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0]
]
for i in picture:
    print('\n')
    for pixels in i:
        if pixels==0:
            print(" ",end='\t')
        elif pixels==1:
            print("*",end='\t')
