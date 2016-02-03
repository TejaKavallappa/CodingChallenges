import math
def isPalindrome(num):
    snum = str(num)
    if snum == snum[::-1]:
        return True
    return False

def isPrime(num):
    rt_i = math.sqrt(num)
    for i in xrange(2,int(rt_i)+1):
        if (num % i == 0):
            return False
    return True

#Find the largest prime palindrome less than 1000
for i in xrange(999,1,-2):
    if (isPrime(i)):
        if (isPalindrome(i)):
            print i
            break

