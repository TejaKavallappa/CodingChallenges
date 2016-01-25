"""
Cases where this doesn't work:
    6 | KHQFM | XQWORO WVMTYN EBCSRV SUHBOJ SLADQO LJUFHK

    Counter({'Q': 1, 'H': 1, 'K': 1, 'M': 1, 'F': 1})
    XQWORO ['Q']
    SLADQO ['Q']
    SUHBOJ ['H']
    WVMTYN ['M']
    LJUFHK ['H', 'K', 'F']
    True

"""
from collections import defaultdict, Counter

filename = "test_alphabetblocks.txt"

with open(filename) as f:
    for test in f:
        print "-------------------"
        print test
        test = test.strip().split("|")
        numblocks = int(test[0])
        word = test[1].strip()
        blocks = test[2].strip().split(" ")
        b_dict = defaultdict(list)
        letter_dict = Counter(word)
        print letter_dict
        no_match = False
        for letter in letter_dict.keys():
            num_matches = 0
            i = 0
            while(i < numblocks):
                if letter in blocks[i]:
                    b_dict[blocks[i]].append(letter)
                    num_matches += 1
                i += 1
            if num_matches < letter_dict[letter]:
                no_match = True
                break
        if no_match:
            print " NO MATCH False"
        elif len(set(b_dict.keys())) < len(word):
            print " SIZE OF KEYS LESS THAN WORD SIZE False"
        else:
            print "True"
