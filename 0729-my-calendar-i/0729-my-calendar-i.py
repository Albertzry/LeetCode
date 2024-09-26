class MyCalendar(object):

    def __init__(self):
        self.times=[]

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if self.times:
            for time in self.times:
                if start<time[1] and time[0]<end:
                    return False
        self.times.append([start,end])
        return True
        
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)