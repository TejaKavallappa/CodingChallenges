def fibonacci(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibonacci(n-2) + fibonacci(n-1)
filename = "test_fibonacci.txt"

with open(filename) as f:
    for test in f:
        test = test.strip()
        n = int(test)
        if n <= 0:
            print 0
            continue
        print fibonacci(n)
        
