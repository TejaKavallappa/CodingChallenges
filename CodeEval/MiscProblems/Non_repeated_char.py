filename = "test_nonrepchars.txt"
with open(filename) as f:
    for test in f:
        res = {} 
        for char in test:
            if (char not in res):
                res[char] = 1
            else:
                res[char] += 1
        for char in test:
            if (res[char] == 1):
                print char
                break

