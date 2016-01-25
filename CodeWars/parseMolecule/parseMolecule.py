class Node:
    def __init__(self, content=None, prev=None):
        self.content = content
        self.prev = prev
    def __str__(self):
        return str(self.content)

def parse_molecule(formula):
    if (formula == None):
        return None
    newForm = formula
    if any(x in formula for x in "(){}"):
        newForm = hasBrackets(formula)
    res = {}
    i = 0
    prev = ""
    while(i < len(newForm)):
        c = newForm[i]
        if (c.isalpha()):
            if (i+1 < len(newForm) and newForm[i+1].islower()):
                c += newForm[i+1]
                i = i +2
            else:
                i+=1
            if(prev and prev not in res):
                res[prev] = 1
            prev = c
        elif (c.isdigit()):
            j = i
            while(j<len(newForm) and newForm[j].isdigit()):
                j+=1
            d = newForm[i:j]
            i=j
            if(prev in res):
                res[prev] += int(d)
            else:
                res[prev] = int(d)
    if(prev.isalpha() and prev not in res):
        res[prev] = 1
    print res
    return res

def hasBrackets(formula):
    #Build tree
    start = 0 
    previous = None
    newNode = None
    for i in xrange(0,len(formula)):
        c = formula[i]
        if (c in "(){}[]"):
            if any(b.isalpha() for b in formula[start:i]):
                newNode = Node(formula[start:i])
                newNode.prev = previous
                previous = newNode
                start = i+1
        if (c in ")}]"): #Closing braces
            if(i+1 < len(formula)):
                d = formula[i+1]
                content = newNode.content
                newcontent = ""
                if d.isdigit():
                    for c in content:
                        if(c.isdigit()):
                            newcontent = newcontent[0:len(newcontent)-1]+str((int(c)*int(d)))
                        else:
                            newcontent+= (c+d)
                    newNode.content = newcontent
                    newNode.prev.content = newNode.prev.content + newcontent
                    newNode = newNode.prev


    newForm = ""
    current = newNode
    while(current != None):
        newForm += current.content
        current = current.prev

    return newForm    

parse_molecule(input()) 
