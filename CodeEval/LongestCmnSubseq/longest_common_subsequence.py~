filename = "test_longest_common_subsequence.txt"

with open(filename) as f:
    for test in f:
        test = test.strip()
        if test == "":
            continue
        str1 = test.split(";")[0]
        str2 = test.split(";")[1]
        print str1, str2
        d = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]
        #Explicitly set to 0
        for i in xrange(len(str1)+1):
            d[i][0] = 0
        for j in xrange(len(str2)+1):
            d[0][j] = 0
        for i in xrange(1, len(str1)+1):
            for j in xrange(1, len(str2)+1):
                if str1[i-1] == str2[j-1]:
                    d[i][j] = d[i-1][j-1] + 1
                else:
                    d[i][j] = max(d[i][j-1],d[i-1][j])
        #print d[len(str1)][len(str2)]
        i = len(d)-1
        j = len(d[0])-1
        res = ""
        while(i > 0 and j > 0):
            if d[i][j] == d[i][j-1]:
                j -= 1
            elif d[i][j] == d[i-1][j]:
                i -= 1
            else:
                res += str1[i-1]
                i -= 1
                j -= 1

        print res[::-1]
