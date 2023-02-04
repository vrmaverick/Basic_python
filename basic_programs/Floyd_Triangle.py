def floyd(n):
    a = 1
    print("Floyd's Triangle") 
    for i in range(1, n + 1):
        for j in range(1, i + 1):        
            print(a, end = '  ')
            a = a + 1
        print()
rows = int(input("Please Enter the total Number of Rows  : "))
floyd(rows)
