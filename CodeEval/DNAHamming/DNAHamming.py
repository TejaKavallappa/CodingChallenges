def hamming_distance(chunk, pat, num_mismatch):
    mismatch = 0
    for ch1, ch2 in zip(chunk, pat):
        if(ch1 != ch2):
            mismatch += 1
            if mismatch > num_mismatch:
                return -1
    return mismatch 

filename = "/Users/teja2/Documents/teja_coding/CodingChallenges/DNAHamming/test_dnahamming.txt"

with open(filename) as f:
    for test in f:
        print "==========================================="
        test = test.split()
        pat = test[0]
        pat_len = len(pat)
        num_mismatch = int(test[1])
        text = test[2]
        i = text.find(pat)
        matches = {}
        duplicates = {}
        for i in xrange(len(text)-pat_len+1):
            chunk = text[i:i+pat_len]
            match_val = hamming_distance(chunk, pat, num_mismatch)
            if(match_val != -1):
                if (chunk in matches):
                    duplicates[chunk] = duplicates.get(chunk,0)+1
                matches[chunk] = match_val
        output = []
        if len(matches)==0:
            print pat, num_mismatch
            print text
            print "No match"
        else:
            for i in xrange(num_mismatch+1):
                vals = [k for k,v in matches.iteritems() if v == i]
                dupes = [entry*(duplicates[entry]) for entry in vals if entry in duplicates]
                vals += dupes
                output += sorted(vals)
            #print " ".join(output)
