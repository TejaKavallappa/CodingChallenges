
filename = "/Users/teja2/Documents/teja_coding/CodingChallenges/ReverseGroups/test_reverse_groups.txt"
with open(filename) as f:
     for test in f:
        if test == "\n":
            continue
        test = test.split(";")
        list_digits = test[0].split(',')
        rotate = int(test[1])
        if len(list_digits)>= rotate:
            i = 0
            while (i+rotate <= len(list_digits)):
                newlist = list_digits[i:i+rotate]
                newlist = newlist[::-1]
                list_digits[i:i+rotate] = newlist
                i += rotate
                if i >= len(list_digits):
                    break
            print ','.join(list_digits)

         
