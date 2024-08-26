class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        n=0
        for i in range(len(s)-1):
            if s[i]!=" " and s[i+1]==" ":
                n+=1
        if s[-1]!=" ":n+=1 
        return n
