print("This program is to find weather the given year is leap year or not")
leap = int(input("Please Enter Year : (YYYY) "))
r = leap % 4
if r==0 :
    if leap%100==0 and leap%400==0 :
        print(leap ,"is a leap year")
    elif leap%100==0 and leap%400!=0 :
        print(leap ,"is not a leap year")
    else :
         print(leap ,"is a leap year")
else:
    print(leap,"is not a leap year")
    if r==1:
        print(leap+3,"will be next leep year")
    elif r==2 :
        print(leap+2,"will be next leep year")
    else:
        print(leap+1,"will be next leep year")
