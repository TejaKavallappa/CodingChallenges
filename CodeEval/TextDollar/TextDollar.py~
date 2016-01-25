numText = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6: 'Six',\
         7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven',\
         12: 'Twelve', 13: 'Thirteen', 14:'Fourteen', 15:'Fifteen',\
         16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen',
         20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty',\
                 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}

fileName = '/Users/teja2/Documents/teja_coding/PYTHON/CodingChallenges/TextDollar/numbers.txt'

           
def tenshundreds(test):
    num = int(test)
    ndigits = len(test)
    result = ""
    if (num == 0):
        return result
    if (ndigits == 3):
        if (test[0] != '0'):
            result += numText[int(test[0])]
            result += "Hundred"
        num = int(test[1:])
        ndigits = len(test[1:])
        test = test[1:]
    if (ndigits == 2):
        if (num in numText):
            result += numText[num]
            return result
        else:
            temp = int(test[0])*10
            if (temp in numText):
                result += numText[temp]
        num = int(test[-1])
        test = test[-1]
    if (num in numText):
        result += numText[num]
    return result


with open(fileName) as f:
    for test in f:
        test = test.rstrip()
        result = ""
        print test
        if (int(test) == 0):
            print "ZeroDollars"
            continue
        ndigits = len(test)
        if (ndigits >= 7 and ndigits < 10):
            result += tenshundreds(test[0:-6])
            result += "Million"
            test = test[-6:] 
            ndigits = len(test)
        if (ndigits >=4 and ndigits <= 6):
            temp = tenshundreds(test[0:-3])
            if (temp != ""):
                result += temp
                result += "Thousand"
            test = test[-3:]
            ndigits = len(test)
        if (ndigits < 4):
            result += tenshundreds(test)
        result += "Dollars"
        print repr(result)
