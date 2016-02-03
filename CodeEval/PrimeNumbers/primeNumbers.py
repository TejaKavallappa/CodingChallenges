#Print out the prime numbers less than a given number N.
# solution should run in N*logN time or less
import math
def isPrime(n):
    for j in xrange(2,int(math.sqrt(n))+1):
        if (n % j == 0):
            return False
    return True

filename = "test_primenumbers.txt"
with open(filename) as f:
    for test in f:
        num = int(test.strip())
        if (num < 3):
            print "\n"
            continue
        primes = [2]
        #check 3,5,..odd numbers until num
        for i in xrange(3, num,2): 
            if (isPrime(i)):
                primes.append(i)

        print ",".join(map(str,primes))
