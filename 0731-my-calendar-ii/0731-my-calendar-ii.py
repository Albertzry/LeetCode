class MyCalendarTwo(object):

    def __init__(self):
        self.times=[]
        self.duplicates=[]

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if self.duplicates:
            for duplicate in self.duplicates:
                if start<duplicate[1] and end>duplicate[0]:
                    return False
        if self.times:
            for time in self.times:
                if start<time[1] and end>time[0]:
                    temp=[max(start,time[0]),min(end,time[1])]
                    self.duplicates.append(temp)
        self.times.append([start,end])          
        return True




# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)