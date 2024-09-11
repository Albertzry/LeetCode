class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        temp = start ^ goal
        temp = str(bin(temp))
        return temp.count("1")