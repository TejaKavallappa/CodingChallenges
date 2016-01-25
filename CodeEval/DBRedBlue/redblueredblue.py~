import re
import collections
import operator

def redblueredblue(pattern, inp):
    memFreq = collections.Counter(pattern)
    print "len = " ,len(memFreq)
    print "sum of values = ",sum(memFreq.values())
    dupInt = inp
    dupPat = pattern
    mapPattern = {}
    if sum(memFreq.values()) == len(memFreq):#All unique keys
        return 1
    print "Dictionary = ", memFreq
    memFreqSorted = sorted(memFreq.items(), key=operator.itemgetter(1), reverse=True)
    for item in memFreqSorted:
        key = item[0]
        val = item[1]
        print key, val
        if inp == "":
            print "Pattern not found"
            return 0
        if val > 1:
            repeat = ".*\\1"*(val-1)
            #pat1 = r"(([a-z]+)?).*\1" 
            pat1 = r"(([a-z]+)?)" + repeat
            print pat1
        else:
            pat1 = r"(([a-z]+)?).*\1" 
        match = re.search(pat1, inp)
        if match:
            print match.group(1)
            mapPattern[key] =match.group(1)
            inp = re.sub(match.group(1),r"", inp)
    if inp != "":
       print "Pattern doesn't match" 
       return 0
    for key in memFreq:
        pattern = re.sub(key,mapPattern.get(key), pattern)
    print pattern
    print dupPat
    if pattern == dupPat:
        return 1
    return 0

if __name__=="__main__":

    pattern = "abcdbbb"
    inp = "tobeornottobebebe"
    result = redblueredblue(pattern, inp)
    
