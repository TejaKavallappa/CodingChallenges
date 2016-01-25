digits = {'1': 0b01100000, '2': 0b11011010, '3': 0b11110010, '4': 0b01100110, '5':0b10110110, '6': 0b10111110, '7': 0b11100000, '8':0b11111110, '9':0b11110110, '0':0b11111100}

#filename = "test_smallbrokenlcd.txt"
filename = "test_brokenlcd.txt"

with open(filename) as f:
    for test in f:
        print
        test = test.split(";")
        number = test[1].strip()
        test = test[0].split(" ")
        test = [int(num, base = 2) for num in test]
        j = 0
        i = 0
        while(i < len(test) and j < len(number)):
            num = number[j]
            digit = digits[num]
            #If next character is a '.' append that to digit
            if((j+1 < len(number)) and number[j+1] == "."):
                digit = digit | 0b00000001
            print number[j],'{:08b}'.format(test[i]), num, '{:08b}'.format(digit)
            if (test[i] & digit == digit):
                if (j+1 < len(number) and number[j+1] == "."):
                    j += 2
                else:
                    j+=1
            i += 1
        if (j == len(number) ):
            print "1", number
            pass
        else:
            print "0", number

        
