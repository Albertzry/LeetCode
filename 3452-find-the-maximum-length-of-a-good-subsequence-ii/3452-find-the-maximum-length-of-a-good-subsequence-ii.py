class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dp = defaultdict(lambda: [0] * (k + 1))
        zd = [0] * (k + 1)

        for v in nums:
            tmp = dp[v]
            for j in range(k + 1):
                tmp[j] += 1
                if j > 0:
                    tmp[j] = max(tmp[j], zd[j - 1] + 1)    
            for j in range(k + 1):
                zd[j] = max(zd[j], tmp[j])
        
        return zd[k]
