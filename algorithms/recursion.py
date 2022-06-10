# recursion: function that calls itself
# base case: decide wheather to stop the recursion and return
# call stack: LIFO

def funcThree():
    print('Three')

def funcTwo():
    funcThree()
    print('Two')

def funcOne():
    funcTwo()
    print('One')

# funcOne()


def factorial(n):
    
    if n == 1:
        return 1
    return n* factorial(n-1)

print(factorial(4))