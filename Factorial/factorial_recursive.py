'''
Computing the factorial of a number using a recursive algorithm

'''

def getFactorial(n):
    if n < 2:
        return 1
    else:
        return n * getFactorial(n - 1)

print(getFactorial(3))
