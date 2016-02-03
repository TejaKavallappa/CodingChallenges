filename = "test_bitpositions.txt"

with open(filename) as f:
    for test in f:
        test = test.strip().split(",")
        num = int(test[0])
        p1 = int(test[1])
        p2 = int(test[2])

        binrep = str(bin(num))[::-1]
        res = binrep[p1-1] == binrep[p2-1]
        print str(res).lower()


