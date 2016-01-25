n = 4
k = 4
arr = [[None for x in range(n+1)] for y in range(k+1)]
guess = [[ 1, 2, 3, 4], [4,3,2,1]]
prob = [1, .25]
for a in xrange(2):
    a1 = guess[a]
    y = 0
    for x in a1:
        print x, y
        if (arr[x][y] == None):
            arr[x][y] = prob[a]
        y += 1


for row in arr:
    row[:] = [x if x != None else 0 for x in row] 
    print row

print arr
arr = zip(*arr)
for row in arr:
    print sum(row)
    if sum(row) > 1:
        print "No"
