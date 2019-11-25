#!/usr/bin/env python3
#1.1
class Fibo:
    def __init__(self):
        self.a = -1
        self.b = 1
        
    def __iter__(self):
        return self
        
    def __next__(self):
        fibo = self.a + self.b
        self.a, self.b = self.b, (self.a + self.b)
        return fibo

f = Fibo()
[next(f) for i in range(10)]

# 1.2
class GenFibo(Fibo):
    
    def __init__(self):
        self.a = 3
        self.b = -1
g = GenFibo()
[next(g) for i in range(10)]


def primes():
    n = 2
    while True:
        if any(n%x==0 for x in range(2,n)) == False:
            yield n
        n+=1
# any: return True of there is one True, all: return True if all return True
# if any((n%x==0 for x in range(2,n)) return False, which means all n%x==0 return False, then it's a prime number, return True
p = primes()
a = [next(p) for i in range(13)]


# 1.4
def ulam():
    t = [1,2]
    u = 3
    while True:
        c = 0
        for j in range(0, len(t)): 
            if (u - t[j]) in t and u != (2*t[j]):  
                c += 1
        if c == 2:   
            t.append(u)
            yield u
        u += 1

u = ulam()
[next(u) for i in range(15)]

# ulam number
# Python3 code to print nth Ulam number  
MAX = 10000
# Array to store Ulam Number  
arr = []  
# function to compute ulam Number  
def ulam(): 
    # Set to search specific Ulam number efficiently  
    s = set()  
    # push First 2 two term of the sequence in the array and set for further calculation  
    arr.append(1)  
    s.add(1)  
    arr.append(2)  
    s.add(2)    
    # loop to generate Ulam number  
    for i in range(3, MAX):  
        count = 0  
        # traverse the array and check if i can be reprsented as sum of two distinct element of the array  
        for j in range(0, len(arr)): 
            # Check if i-arr[j] exist in the array or not using set. If yes, Then i can be represented as sum of arr[j] + (i- arr[j])  
            if (i - arr[j]) in s and arr[j] != (i - arr[j]):  
                count += 1  
            # if Count is greater than 2 break the loop  
            if count > 2:  
                break          
        # If count is 2 that means i can be represented as sum of two distinct terms of the sequence  
        if count == 2: 
            # i is ulam number  
            arr.append(i)  
            s.add(i)  
          
# Driver Code     
if __name__ == "__main__":  
    # pre compute Ulam Number sequence  
    ulam()    
    n = 9 
    # print nth Ulam number  
    print(arr[n - 1])  
  
# This code is contributed by Rituraj Jain 

# 2.1
pow2minus1 = [2**n-1 for n in range(1,21)]


# 2.2
# define a generator that enumerates the non-negative integers
def non_integer():
    n = -1
    while True:
        n = n + 1
        yield n

# generator expression
caterer = ((n**2+n+2)/2 for n in non_integer())
next(caterer)

# generator
def lazy():
    n = 0
    while True:
        (h,n) = ((n**2+n+2)/2, n+1)
        yield h
l = lazy()
[next(l) for x in range(10)]



# 2.3
# define a generator that enumerates the positive integers
def positive():
    n = 0
    while True:
        n = n + 1
        yield n


# generator expression
tetra = (n*(n+1)*(n+2)/6 for n in positive())
next(tetra)

# generator
def tetrahedral():
    n = 1
    while True:
        (h,n) = (n*(n+1)*(n+2)/6, n+1)
        yield h
t = tetrahedral()
[next(t) for x in range(10)]


# 3.1
import functools
sum_of_even_squares = functools.reduce(lambda x,y: x+y, filter(lambda x: x%2 == 0, [x*x for x in range(1,21)]))


# 3.2
p = primes()
product_of_primes = functools.reduce(lambda x,y: x*y, [next(p) for i in range(13)])


# 3.3
p = primes()
squared_primes = functools.reduce(lambda x,y: x+y, [x*x for x in [next(p) for i in range(31)]])


# 3.4
harmonics = [functools.reduce(lambda x,y: x+1/y, range(i)) for i in range(2,22)]
# set range to (2,22), so the first range will be range(2) to range(21)

# 3.5
tetra = (n*(n+1)*(n+2)/6 for n in positive())
tetra_geom = [functools.reduce(lambda x,y: x*y, [next(tetra) for x in range(12)])][0]**(1/12)



# 4.1
def make_poly(coeffs):
    s = 0
    return lambda x: sum(i * (x ** k) for k,i in enumerate(coeffs))

make_poly([1,2,2,3])(2)



# 4.2
def eval_poly(coeffs, args):
    return [make_poly(coeffs)(i) for i in args]

coeffs = [1,2,2,3]
args = [1,2,3]
eval_poly(coeffs, args)













