class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i=0
        while True:
            if i**2<=x and (i+1)**2>x:
                return i
            i+=1