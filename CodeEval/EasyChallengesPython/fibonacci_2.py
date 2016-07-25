
n = int(raw_input().strip())
if n <= 1:
    fibo = [0]
elif n == 2:
    fibo = [0,1]
else:
    fibo = [0,1]
    for i in xrange(3,n+1):
        fibo.append(fibo[-1]+fibo[-2])
print fibo
cube = lambda p : p*p*p     
fibo2 = map(cube, fibo)
print fibo2

