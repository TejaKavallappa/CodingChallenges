c = int(raw_input("Enter the number of test cases:"))

for testNum in xrange(0,c):
    nkq = raw_input("Enter n, k and q, separated by a single space:")
    nkq = nkq.split(' ')
    n = int(nkq[0])
    k = int(nkq[1])
    q = int(nkq[2])
    
    arr = [[None for x in range(n+1)] for y in range(k+1)]
    guesses = []
    scores = []
    count = 0
    conflict = 0
    for num in xrange(q):
        guess = raw_input("Enter the guess: ")
        guess = guess.split(' ')
        guesses.append(guess[0:-1])
        score = int(guess[-1])
        scores.append(score)
        count += 1
        y = 0
        prob = score*1.0/k
        print guess[0:-1]
        for x in guess[0:-1]:
            x = int(x)
            print x, y
            if (arr[x][y] == None):
                arr[x][y] = prob
            else:
                conflict += 1
            y += 1
    for row in arr: 
        row[:] = [x if x != None else 0 for x in row]
        print row

    arr = zip(*arr)
    for row in arr:
        print sum(row)
        if sum(row) > 1:
            print "No"
