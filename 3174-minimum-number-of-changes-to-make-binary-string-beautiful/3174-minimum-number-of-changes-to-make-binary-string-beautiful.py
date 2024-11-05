class Solution(object):
    def minChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 1
        ans=0
        while i <len(s):
            if not s[i]==s[i-1]:
                ans+=1
            i+=2
        return ans