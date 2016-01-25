from math import radians, sin, cos, atan2, sqrt
import re
import random
class Point:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
    def distance_to(self, another):
        # Earth's radius = 6371 km
        phi1 = radians(self.latitude)
        phi2 = radians(another.latitude)
        lambda1 = radians(self.longitude)
        lambda2 = radians(another.longitude)
        del_phi = phi2-phi1
        del_lambda = lambda2-lambda1
        a = sin(del_phi/2)*sin(del_phi/2) + cos(phi1)*cos(phi2)*sin(del_lambda/2)*sin(del_lambda/2)
        c = 2* atan2(sqrt(a), sqrt(1-a))
        return 6371*c
    def __repr__(self):
        return str(self.latitude) +  "," + str(self.longitude)


class TimeStamp:
    def __init(self):
        a = 1

class Placemark:
    def __init__(self, name, timestamp, loc):
        self.name = name
        self.timestamp = timestamp
        self.loc = loc 
    def __repr__(self):
        #return self.name + " " + self.timestamp + " " + self.loc.__repr__()
        return self.name
    def __eq__(self,other):
        return (self.name == other.name)
    def __hash__(self):
        return hash(self.name)
    def getName(self):
        newname = self.name.split(" ")[-1]
        return newname

#filename = "test_flight370.txt"
filename = "cp_malaysiaairsar2014_crowdrank.kmz"

inPlacemark = False
placemark_names = {}
reference_points = {}
name = ""
timestamp = ""
point = None 
count = 0
radius = 0
search_point = Point(0.0,0.0) 
candidate_placemarks={}
with open(filename) as f:
    for test in f:
        test = test.strip()
        if ('<' not in test):
            if (test.strip() == ""):
                continue
            test = test.split(";")
            radius = int(test[0])
            test = re.sub(r"[\(\)]", "", test[1])
            test = test.split(",")
            search_point = Point(float(test[0]), float(test[1]))
            candidate_placemarks[search_point]=[]
            print search_point, radius
            reference_points[search_point] = radius
        if ("<Placemark" in test):
            inPlacemark = True
        elif ("<name" in test and inPlacemark):
            match = re.search(r"<name>(.+)</name>", test)
            if (match):
                name = match.group(1)
        elif ("<when" in test and inPlacemark):
            match = re.search(r"<when>(.+)</when>",test)
            if (match):
                timestamp = match.group(1)
        elif ("<coordinates" in test and inPlacemark):
            match = re.search(r"<coordinates>(.+)</coordinates>",test)
            if (match):
                str_pt = match.group(1).split(",")
                point = Point(float(str_pt[0]), float(str_pt[1]))
        elif ("</Placemark" in test):
            if (point is not None and timestamp != ""):
                plm = Placemark(name, timestamp, point)
                #Calculate distance b/w this point and all reference points
                for key in reference_points:
                    dist_ref = point.distance_to(key) 
                    if (dist_ref <= reference_points[key]):
                        candidate_placemarks[key].append(plm)
                        print name,dist_ref
            count += 1
            name = ""
            timestamp = ""
            point = None
            inPlacemark = False
print count
count = 1
for key in candidate_placemarks:
    print "----------------------"
    print count
    print key, len(candidate_placemarks[key])
    candidates = [plmk for plmk in candidate_placemarks[key]]
    #print len(set(candidates))
    name_dict = {}
    for can in candidates:
        if (can not in name_dict):
            name_dict[can.getName()] = 1
            print can.getName()
        else:
            name_dict[can.getName()] += 1
            print can.getName()
    count += 1
#print [entry for entry in placemark_names if placemark_names[entry]>1]
