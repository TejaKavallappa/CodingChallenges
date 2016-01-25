from collections import defaultdict
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def generate_combination(elements, length):
    for i in xrange(len(elements)):
        if length == 1: 
            yield (elements[i],)
        else:
            for elem in generate_combination(elements[i+1:len(elements)],length-1):
                yield (elements[i],) + elem
 
def collinear(a, b, c):
    det = a.x*(b.y - c.y) - b.x*(a.y - c.y) + c.x*(a.y - b.y)
    if (det == 0):
        return True
    return False

def slope (a, b):
    if (b.x - a.x == 0):
        return float("inf")
    return (b.y - a.y)*1.0/(b.x - a.x)

def overlap(lla, lb):
    """Return true if at least two elements overlap"""
    #check if it's a list of lists
    if not any(isinstance(i, list) for i in lla):
        return any(i in lla for i in lb)
    else:
        for i in lla:
            if isinstance(i, list):
                return nested_list(i,lb)
         
def nested_list(la, lb):
    return any(i in la for i in lb)
        

filename = "test_straightlines.txt"
with open(filename) as f:
    clength = 3 #Consider 3 points at a time
    for test in f:
        test = test.strip()
        test = test.split("|")
        length = len(test)
        if length < 3:
            print "0"
            continue
        #Generate all combinations with 3 points
        elements = list(range(length))
        combos = list(generate_combination(elements, clength))
        pt_array = [None]*length
        for i in xrange(length):
            pt_test = test[i].strip().split(" ")
            pt_array[i] = point(int(pt_test[0]),int(pt_test[1]))
        res = 0    
        slope_dict = defaultdict(list) 
        for combo in combos:
            if (collinear(pt_array[combo[0]],pt_array[combo[1]],pt_array[combo[2]])) :
                #tpts = " ".join([str(combo[0]),str(combo[1]),str(combo[2])])
                tpts = [str(combo[0]),str(combo[1]),str(combo[2])]
                slope_val = slope(pt_array[combo[0]],pt_array[combo[1]])
                slope_val = round(slope_val,4)
                if (not overlap(slope_dict[slope_val], tpts)):
                    slope_dict[slope_val].append(tpts)
                    res += 1
        print slope_dict
        print res


