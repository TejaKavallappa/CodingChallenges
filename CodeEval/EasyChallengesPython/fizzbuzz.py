filename = "test_fizzbuzz.txt"

with open(filename) as f:
    for test in f:
        test = test.strip().split(" ")
        fizz = int(test[0])
        buzz = int(test[1])
        lim = int(test[2])
        res = ""
        for i in xrange(1,lim+1):
            if (i % fizz == 0 and i % buzz == 0):
                res += "FB "
            elif (i % fizz == 0):
                res += "F "
            elif (i % buzz == 0):
                res += "B "
            else:
                res += str(i)+ " "
        print res[:-1]
