filename = "test_mtolastelement.txt"

with open(filename) as f:
    for test in f:
        steps = int(test.split(" ")[-1])
        lst = test.split(" ")[0:-1]
        print steps, lst
        if (steps > len(lst)):
            print ""
            continue
        print lst[len(lst) - steps]

