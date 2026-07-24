class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        m = max(nums)
        u = 1
        while u<=m:
            u<<=1
        
        n = len(nums)
        t = [False]*u
        for i in range(n):
            for j in range(i,n):
                t[nums[i]^nums[j]] = True
        
        s = [False]*u
        for x in range(u):
            if not t[x]:
                continue
            for k in range(n):
                s[x^nums[k]] = True

        ans = 0
        for r in s:
            ans +=1 if r else 0
        return ans