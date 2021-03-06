import re

map_text_num = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, \
        "six":6, "seven":7, "eight":8, "nine":9, "ten":10, "eleven":11, \
        "twelve":12, "thirteen":13, "fourteen":14, "fifteen":15, "sixteen":16,
        "seventeen":17, "eighteen":18, "nineteen":19, "twenty":20, "thirty":30,
        "forty":40, "fifty":50, "sixty":60, "seventy":70, "eighty":80, "ninety":90,
        "hundred":100, "thousand":1000, "million":1000000}

def hundreds_tens(list_nums):
    temp = 0
    if("hundred" in list_nums):
        num = list_nums.index("hundred") -1
        temp += map_text_num[list_nums[num]]*100
        list_nums = list_nums[num+2:]
    if (len(list_nums) != 0):
        for num in list_nums:
            temp += map_text_num[num]
    return temp
    
filename = "test_textnumber.txt"
with open(filename) as f:
    for test in f:
        test = test.rstrip()
        if (test == ""):
            continue
        print test
        res = 0 
        sign = 1
        #Look for negative
        if (test.split(" ")[0] == "negative"):
            sign = -1
            test = re.sub(r"negative ", "", test)
        test = test.split(" ")
        if("million" in test):
            idx = test.index("million")
            mill = test[0:idx]
            test = test[idx+1:]
            temp = hundreds_tens(mill)
            res += temp*1000000
        if("thousand" in test):
            idx = test.index("thousand")
            thou = test[0:idx]
            temp = hundreds_tens(thou)
            res += temp*1000
            test = test[idx+1:]
        if (len(test)>0):    
            res += hundreds_tens(test)    

        print res*sign
