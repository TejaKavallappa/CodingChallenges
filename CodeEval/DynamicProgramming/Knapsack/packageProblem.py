filename = "./test_packageProblem.txt"

with open(filename) as f:
    for test in f:
        arr1 = test.strip().split(":")
        max_weight = int(arr1[0])
        arr2 = arr1[1].strip().split(" ")
        num_items = len(arr2)
        wt = [0] * (num_items+1)
        val = [0] * (num_items+1)
        i = 0
        for package in arr2:
            i += 1
            package = package.translate(None,"()")
            package = package.split(",")
            wt[i] = float(package[1])
            val[i] = int(package[2].translate(None,"$"))
        print wt    
        #K(w,j): maximize value, 0<=j <= num items
        k = [[0 for i in range(max_weight+1)] for j in range(num_items+1)]
        for j in xrange(num_items+1):
            k[j][0] = 0
        for w in xrange(max_weight + 1):
            k[0][w] = 0
        for j in xrange(1, num_items+1): #Number of items
            for w in xrange(1, max_weight+1):
                if wt[j] > w:
                    k[j][w] = k[j-1][w]
                else:
                    k[j][w] = max(k[j-1][w], k[j-1][int(w-wt[j])] + val[j])
        print k[num_items][max_weight]
        res = ""
        i = num_items
        j = max_weight
        prev = 0 
        while(i > 0 and j > 0):
            if (k[i][j] == k[i-1][j]):
                i -= 1
            elif (k[i][j] == k[i-1][int(j-wt[i])] + val[i]):
                print val[i], wt[i], i
                j = int(j - wt[i])
                if prev != i:
                    res += str(i)
                    prev = i
        print res
