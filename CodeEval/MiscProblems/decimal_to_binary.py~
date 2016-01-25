filename = "test_decimaltobinary.txt"

with open(filename) as f:
    for test in f:
        dec = int(test.strip())
        binary = ""
        if dec == 0:
            binary = "0"
        while(dec > 0):
            binary += str(dec%2)
            dec = dec/2
        print binary[::-1]
