pascal = [1]
prevline = pascal
size = 5 
while(size > 1):
    size -= 1;
    newline = [None]*(len(prevline)+1)
    newline[0] = 1
    newline[-1] = 1
    for i in xrange(1,len(prevline)):
        newline[i] = prevline[i]+prevline[i-1]
    pascal.extend(newline)
    prevline = newline

print " ".join(str(x) for x in pascal)
