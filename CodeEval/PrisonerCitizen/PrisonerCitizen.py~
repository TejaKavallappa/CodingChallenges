class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return str(self.x) + " " + str(self.y)

def does_intersect(a, b, c, d):
    ccw1 = orientation(a, b, c)
    if (ccw1 == 0): 
        #check if c actually lies on the segment
        if((c.x > a.x and c.x < b.x) or (c.x > b.x and c.x < a.x)):
            return 0 
        if ((c.y > a.y and c.y < b.y) or (c.y > b.y and c.y < a.y)):
            return 0
    ccw2 = orientation(a, b, d)
    if (ccw1 == ccw2):
        return -1 #Both pts c, d lie on the same side of segment ab
    ccw3 = orientation(c, d, a)
    ccw4 = orientation(c, d, b)
    if (ccw3 == 0 or ccw4 == 0):
        return -2 #Segment cd intersects the polygon at a vertex
    if (ccw3 == ccw4):
        return -1 #Both pts a, b lie on the same side of segment cd
    return 1

def orientation(a, b, c):
    det = a.x*(b.y - c.y) - b.x*(a.y - c.y) + c.x*(a.y - b.y)
    if (det < 0):
        return -1
    elif (det > 0):
        return 1
    return 0

filename = "/Users/teja2/Documents/teja_coding/PYTHON/CodingChallenges/PrisonerCitizen/testing.txt"
with open(filename) as f:
    for test in f:
        print "=============================="
        print test
        pc_xy = test.rstrip().split("|")[1].split()
        checkPt = Point(int(pc_xy[0]),int(pc_xy[1]))
        extremePt = Point(11, int(pc_xy[1]))
        polyxy_pts = test.rstrip().split("|")[0].split(",")
        polygonPts = [] 
        for pt in polyxy_pts:
            xyVal = pt.split()
            newPt = Point(int(xyVal[0]),int(xyVal[1]))
            polygonPts.append(newPt)
        if (checkPt in polygonPts):
            print "Prisoner"
            continue
        polygonPts.append(polygonPts[0]) #To include all line segments
        num_intersection = 0
        pt_intersection = 0
        decision = ""
        res = 0
        for i in xrange(len(polygonPts)-1):
            if (res == -2): #Check if the point lies inside the polygon
                o1 = orientation(polygonPts[i-1], polygonPts[i],checkPt)
                o2 = orientation(polygonPts[i], polygonPts[i+1], checkPt)
                print o1, o2 , "o1,o2"
                if (o1 == o2):
                    num_intersection += 1
                res = 0
                continue
            res = does_intersect(polygonPts[i], polygonPts[i+1], checkPt, extremePt)
            if res == 0:
                decision = "Prisoner"
                break
            if (res == 1):
                num_intersection += 1
            print "Num intersection =", num_intersection
        if decision == "":
            if (num_intersection % 2 == 1):
                decision = "Prisoner"
            else:
                decision = "Citizen"
        print decision
