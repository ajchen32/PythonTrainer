# Add all numbers from 1 to n and return the sum

# output instructions function
def instructions():
    return "Add all numbers from 1 to n (inclusive) and return the sum" 

# this should have problems and their solutions
def makeTestCases(): 
    sums = dict()
    for i in range(1, 11):
        n = 1
        s = 0
        while n <= i:
           s += n
           n += 1
        sums[i] = s
    return sums


    