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
    for j in i:
        if j==0:
            print(" ",end='\t')
        elif j==1:
            print("*",end='\t')
