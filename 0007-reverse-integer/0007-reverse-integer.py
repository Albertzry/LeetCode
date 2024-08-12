class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x>=0:
            x = str(x)
            t=1
        else:
            x = str(x)[1:]
            t=0
        result = ""
        i = len(x) - 1
        while i >= 0:
            result += x[i]
            i-=1
        if t==1:
            result = int(result)
        else:
            result = -int(result)
        if result>-1+2**31 or result<-2**31:
            return 0
        return result
            