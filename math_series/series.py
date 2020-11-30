def fibonacci(n):
    '''
     Create a function called fibonacci. The function should have one parameter n.
     The function should return the nth value in the fibonacci series. 
     implimenting function using : recursion.
     The Rule is xn = xn−1 + xn−2 
    '''
    if n <= 1:
        if n == 0:
            return 0
        else:
            return 1
    
    return fibonacci(n-1) + fibonacci(n-2)


# _________________________________________

def lucas(n):
    '''
    Creating function lucas that returns the nth value in the lucas numbers 
    implimenting function using : recursion.
    How to get the sequence for the lucas series ==> The Rule is : fibonacci(n) = L(n-1) + L(n+1) for all integers n
    '''
    if n <= 1:
        if n == 0:
            return 2
        else:
            return 1

    return lucas(n-1) + lucas(n-2)

print(lucas(5))


#______________________________________________

def sum_series(n,x=0,y=1):
    '''
    Creating a function that checks if the input is fibonacci OR lucas
     // if NOT return a new series with the new input

    '''
    if x == 2 and y == 1:
        return lucas(n)
    elif x == 0 and y == 1:
        return fibonacci(n)

    else:
        return fibonacci(n) + lucas(x)

      