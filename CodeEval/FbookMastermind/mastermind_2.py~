filename = "test_mastermind.txt"
with open(filename) as f:

    numcases = f.readline()
    numcases = int(numcases)
    for i in xrange(numcases):
        nkq = f.readline().strip() #n,k,q
        nkq = nkq.split(" ")
        #print nkq
        n = int(nkq[0])#Maximum digit value 1<= n <= 11
        k = int(nkq[1])#Number of integers in guess
        q = int(nkq[2])
        prob_mat = [[None for x in range(k)] for y in range(q)]
        guess_mat= [[None for x in range(k)] for y in range(q)]
        print prob_mat
        no_chance = []
        winner = []
        score_mat = [None]*q
        for j in xrange(q):
            guess = f.readline()
            guess = guess.split(" ")
            guess_mat[j] = guess[0:-1]
            score_mat[j] = int(guess[-1])
        print guess_mat
        print score_mat
        if (0 in score_mat):
            idx = score_mat.index(0)
            prob_mat[idx] = [0]*k
            for row in xrange(len(guess_mat)):
                if (row == idx):
                    continue
                for col in xrange(k):
                    if (guess_mat[row][col] == guess_mat[idx][col]):
                        prob_mat[row][col] = 0
            print prob_mat
        if (k in score_mat): #Perfect score
            idx = score_mat.index(k)
            prob_mat[idx] = [1]*k
            for row in xrange(len(guess_mat)):
                if (row == idx):
                    continue
                for col in xrange(k):
                    if (guess_mat[row][col] == guess_mat[idx][col]):
                        prob_mat[row][col] = 1 
        
        for row in xrange(len(prob_mat)):
            #print prob_mat[row], score_mat[row], row
            if(score_mat[row] != 0 and score_mat[row] != k):
                num_nones = prob_mat[row].count(None)
                prob = score_mat[row]*1.0/num_nones
                for col in xrange(k): 
                    if prob_mat[row][col] == None:
                        prob_mat[row][col] = prob

        #print prob_mat 
        sum_probs =  [0]*k
        for i in xrange(q):
            sum_probs = [sum_probs[i] + prob_mat[i][j] for j in xrange(k)]
        #print sum_probs
        if not all(i <= 1 for i in sum_probs):
            print "No"
        else:
            print "Yes"
