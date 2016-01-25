class Time(object):
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def __repr__(self):
        return '%02d'%self.hour+":"+'%02d'%self.minute+":"+'%02d'%self.second
    def __lt__(self, other):
        if(self.hour < other.hour):
            return True
        elif(self.hour == other.hour):
            if(self.minute < other.minute):
                return True
            elif(self.minute == other.minute):
                if(self.second < other.second):
                    return True
        return False
    def __eq__(self, other):
        return (self.hour == other.hour and self.minute == hour.minute and self.second == other.second)
    def __gt__(self, other):
        if(self.hour > other.hour):
            return True
        elif(self.hour ==  other.hour):
            if(self.minute > other.minute):
                return True
            elif(self.minute == other.minute):
                if(self.second > other.second):
                    return True
        return False

filename = "test_timestamp.txt"

with open(filename) as f:
    for test in f:
        print test
        timeStamps = test.split()
        feedTime = []
        for ts in timeStamps:
            hms = ts.split(":")
            tObj = Time(int(hms[0]), int(hms[1]), int(hms[2]))
            feedTime.append(tObj)
        feedTime.sort()
        feedTime.reverse()
        print " ".join(map(str, feedTime))

