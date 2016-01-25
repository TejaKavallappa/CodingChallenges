filename = "test_checkparentheses.txt"

closeb = {"(":")","{":"}","[":"]"}
with open(filename) as f:
    for test in f:
        test = test.strip()
        print test
        stack = []
        match = True
        for bracket in test:
            if bracket in closeb:
                stack.append(bracket)
            else:
                if not stack or bracket != closeb.get(stack.pop()):
                    match = False
                    break
        if match and stack:
            match = False
        print match
