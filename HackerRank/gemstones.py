n = int(raw_input())
gem = set("abcdefghijklmnopqrstuvwxyz")
for i in xrange(n):
    st = raw_input()
    print set(st)
    gem = (gem & set(st))
    print gem
print len(gem)    

