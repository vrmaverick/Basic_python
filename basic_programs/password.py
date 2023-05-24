user=input("username : ")
password = input("password : ")
if password=='admin' :
    pas = '*'*len(password)
    print("Hello user: {} your password {} of length {} is correct you can proceed ahead ".format(user,pas,len(pas)))
else:
    pas = '*'*len(password)
    print("Hello user: {} your password {} of length {} is incorrect try again".format(user,pas,len(pas)))
