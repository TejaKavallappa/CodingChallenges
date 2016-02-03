filename = "test_pangrams.txt"

with open(filename) as f:
    for test in f:
        pan_arr = [False]*26
        for letter in test:
            if (letter == ' '):
                continue
            if (ord(letter) > 96 and ord(letter)< 123):
                pan_arr[ord(letter)-97] = True
            if (ord(letter) < 91 and ord(letter) > 64):
                pan_arr[ord(letter) - 65] = True
        res = [chr(i + 97) for i in xrange(len(pan_arr)) if pan_arr[i] == False]
        if res == []:
            print "NULL"
        else:
            print "".join(res)
