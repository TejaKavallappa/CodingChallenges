filename = "test_multiplesofexp2.txt"

with open(filename) as f:
    for test in f:
        print test
        test = test.strip().split(",")
        num = int(test[0])
        pow2 = int(test[1])
        res = pow2
        while(res < num):
            res += pow2 
        print res 
