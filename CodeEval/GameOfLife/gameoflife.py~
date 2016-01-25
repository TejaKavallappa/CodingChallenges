#Alive: *
#Dead: .

filename = "test_gameoflife.txt"

SIZE = 10+2
grid_now = [[None]*SIZE for i in xrange(SIZE) ]
with open(filename) as f:
    i = 1 
    for test in f:
        test = test.strip()
        grid_now[i][1:SIZE-1] = list(test)
        print grid_now[i]
        i += 1

for i in xrange(1, len(grid_now)-1):
    print "".join(grid_now[i][1:SIZE-1])

for run in xrange(10):
    print
    new_grid = [[None]*SIZE for i in xrange(SIZE)]
    for i in xrange(1,len(grid_now)-1):
        for j in xrange(1, len(grid_now)-1):
            neighbors = [grid_now[i-1][j-1], grid_now[i-1][j],grid_now[i-1][j+1]]
            neighbors.extend([grid_now[i][j-1],grid_now[i][j+1]])
            neighbors.extend([grid_now[i+1][j],grid_now[i+1][j+1],grid_now[i+1][j-1]])
            state = grid_now[i][j]
            num_n = neighbors.count('*')
            if (state == '.' and num_n == 3):
                new_grid[i][j] = '*'
            elif (state == '*' and (num_n < 2 or num_n > 3)):
                new_grid[i][j] = '.'
            elif (state == '*' and  (num_n ==2 or num_n == 3)):
                new_grid[i][j] = '*'
            else:
                new_grid[i][j] = state
    grid_now = new_grid

    for i in xrange(1, len(grid_now)-1):
        print "".join(grid_now[i][1:SIZE-1])


