filename = "test_reversewords.txt"

with open(filename) as f:
    for test in f:
        if test == "":
            continue
        test = test.strip().split(" ")
        print " ".join(test[::-1])
