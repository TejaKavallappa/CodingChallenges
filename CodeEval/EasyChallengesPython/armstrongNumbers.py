filename = "test_armstrongNumbers.txt"

with open(filename) as f:
    for test in f:
        num = test.strip()
        num_sum = 0
        exp = len(num)
        for digit in num:
            num_sum += int(digit)**exp
        print str(num_sum) == num

