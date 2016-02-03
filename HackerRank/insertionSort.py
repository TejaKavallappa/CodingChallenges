def insertionSort(ar):
    v = ar[-1]
    for i in xrange(len(ar)-2,-1,-1):
        if (ar[i] > v):
            ar[i+1] = ar[i]
            print " ".join(map(str,ar))
        elif ar[i] <= v:
            ar[i+1] = v
            print " ".join(map(str,ar))
            break
        if i == 0:
            ar[i] = v
            print " ".join(map(str,ar))


m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)

