import re
filename = "test_ipaddressintruder.txt"
with open(filename) as f:
    for test in f:
        test = test.strip()
        print
        #print test
        match = re.search(r"[10]{31,32}", test)
        if(match):
            print match.group()

