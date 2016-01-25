filename = "test_asciidecrypt.txt"

with open(filename) as f:
    for test in f:
        print test
        length = int(test.split("|")[0].strip())
        alpha =  test.split("|")[1].strip()
        test = test.split("|")[2].split()
        ascii_nums = [int(val) for val in test]
        space_val = min(ascii_nums)
        shift = space_val - ord(' ')
        modified_ascii = [int(val)-shift for val in test]
        sentence = [chr(val) for val in modified_ascii]
        print "".join(sentence)
