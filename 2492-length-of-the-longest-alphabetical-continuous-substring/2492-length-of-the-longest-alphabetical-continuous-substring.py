class Solution(object):
    def longestContinuousSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res,i,n,current=1,1,len(s),1
        while i <n:
            if ord(s[i])==ord(s[i-1])+1:
                current+=1
                res = max(res,current)
            else:
                current=1
            i+=1
        return res