def sum(num1,num2):
    '''
     Info: This function returns another function which returns the sum
    '''
    def another_function(n1,n2):
        return n1 + n2
    return another_function(num1,num2)
print(sum(10,20))
print(sum.__doc__)
#cannot call another function directly from main
