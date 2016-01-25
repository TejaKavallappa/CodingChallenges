def is_palindrome(num):
    return num == num[::-1]

filename = "test_reverse_add.txt"

#with open(filename) as f:
#    for test in f:
    num = test.strip()
    count = 0
    while(count < 100):
        int_num = int(num)
        rev_num = int(num[::-1])
        sumn = int_num + rev_num
        num = str(sumn)
        count += 1
        if is_palindrome(str(sumn)):
            print count, sumn
            break
