import re
class thing:
    def __init__(self, index, weight, price):
        self.index = index
        self.weight = weight
        self.price = price
    def __repr__(self):
        return self.index + " " + str(self.weight) + " " + str(self.price)

filename = "/Users/teja2/Documents/teja_coding/CodingChallenges/PackageProblem/test_packages.txt"

with open(filename) as f:
    for test in f:
        list_things = []
        max_weight = int(test.split(":")[0])
        objs = test.split(":")[1].split()
        for obj in objs:
            obj = re.sub(r"[\(\)\$]","",obj)
            obj = obj.split(",")
            if (float(obj[1]) <= max_weight):
                new_thing = thing(obj[0], float(obj[1]), int(obj[2]))
                list_things.append(new_thing)
        print max_weight
        if(len(list_things) == 0):
            print "-"
            continue
        list_things = sorted(list_things, key=lambda athing: athing.weight, reverse=True)
        print list_things
        max_price = list_things[0].price
        max_object = [list_things[0]]
        for i in xrange(len(list_things)):
            for j in xrange(i+1, len(list_things)):
                if (list_things[j].price > max_price):
                    max_price = list_things[j].price
                    max_object = [list_things[j]]
                if (list_things[i].weight + list_things[j].weight < max_weight):
                    if (list_things[i].price + list_things[j].price > max_price):
                        max_price = list_things[i].price + list_things[j].price
                        max_object = [list_things[i],list_things[j]]
                    elif (list_things[i].price + list_things[j].price == max_price):
                        if(list_things[i].weight + list_things[j].weight < sum(thg.weight for thg in max_object)):
                            max_object = [list_things[i],list_things[j]]
        max_object = sorted(max_object)                    
        print ",".join([i.index for i in max_object])
