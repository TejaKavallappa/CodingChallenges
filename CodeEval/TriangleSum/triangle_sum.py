filename = "smalltriangle.txt"

with open(filename) as f:
    for test in f:
        test = test.strip()
        if test == "":
            continue
        print test
