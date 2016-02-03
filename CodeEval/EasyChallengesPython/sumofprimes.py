import math
def isPrime(num):
    rt_i = math.sqrt(num)
    for i in xrange(2,int(rt_i)+1):
        if (num % i == 0): 
            return False
    return True
res = 2
j = 1
i = 3
while(j < 1000):
    if isPrime(i):
        res += i
        j += 1
    i += 2
print res
