while True:
    try:
        year = int(input("Enter your year of birth : "))
        i = 10/year
    except ValueError:  # only for value error
        print('Enter a number not a string')
 except ZeroDivisionError as err:
        print('number cannot be 0')
        print(err) #display error
    except:
        print("for all other errors")
        break
    else:
        print("no errors detected while loop terminates here!!!!!!!!", i)
        break
    finally:
        print('this will print whatever happens')
