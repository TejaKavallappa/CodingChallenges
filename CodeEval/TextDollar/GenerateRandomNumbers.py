import random

filename = "numbersRand.txt"
with open(filename, "w") as f:
    for i in xrange(20):
        f.write(str(random.randrange(0,10001))+'\n')
        f.write(str(random.randrange(10001, 1000000001)) + '\n')
f.close()
