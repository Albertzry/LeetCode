class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        rec=defaultdict(list)
        for i,ch in enumerate(s):
            rec[ch].append(i)
        ans=0
        for key in rec:
            if len(rec[key])%2==0:
                ans+=2
            else:
                ans+=1
        return ans