class Solution(object):
    def maxCount(self, banned, n, maxSum):
        """
        :type banned: List[int]
        :type n: int
        :type maxSum: int
        :rtype: int
        """
        banned=set(banned)
        all=0
        ans=0
        for i in range(1,n+1):
            if i not in banned:
                if all+i<=maxSum:
                    ans+=1
                    all+=i
                else:
                    break
        return ans