#Incomplete
from Queue import PriorityQueue


def makeDict(string):
    char_dict = {}
    for i in string:
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1
    return char_dict


filename = "test_huffmanCoding.txt"

with open(filename) as f:
    for test in f:
        freq = makeDict(test.strip())
        tree = PriorityQueue(len(freq))
        print freq
        for key in freq:
            tree.put((key,freq[key]))
        while not tree.empty():    
            print tree.get()



