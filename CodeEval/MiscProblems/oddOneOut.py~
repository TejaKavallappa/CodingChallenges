filename = "test_oddoneout.txt"

with open(filename) as f:
    for test in f:
        test = test.strip().split(";")
        size = int(test[0])
        arr = test[1].split(",")
        num = int(arr[0]) + 1
        for i in xrange(1,size):
            num = num ^ (int(arr[i]) + 1) ^ i
        print num-1 


