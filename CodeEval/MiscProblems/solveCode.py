import sys
top_arr = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m']
bottom_arr = [' ','u','v','w','x','y','z','n','o','p','q','r','s','t']
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    res = ""
    test = test.strip()
    for letter in test:
        if (letter == " "):
            res += " "
            continue
        idx = ord(letter) - 96
        if (idx < 14):
            res += bottom_arr[idx]
        elif (idx > 20 and idx < 27):
            res += top_arr[idx-20]
        elif (idx >13 and idx < 21):
            res += top_arr[idx - 7]
    print res, test
test_cases.close()

