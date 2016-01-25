import operator
filename = "test_names_unique.txt"

name_dict = {}
with open(filename) as f:
    bigString = f.read()
    bigString = bigString.split(",")
    print len(bigString)
    for place in bigString:
        place = place.split(" ")
        if (place[-1] in name_dict):
            name_dict[place[-1]] += 1
        else:
            name_dict[place[-1]] = 1


print min(name_dict.iteritems(), key =operator.itemgetter(1))
