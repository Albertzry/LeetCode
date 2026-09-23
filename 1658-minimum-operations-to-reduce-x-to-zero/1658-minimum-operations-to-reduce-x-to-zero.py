class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        s = sum(nums)
        n = len(nums)
        length = 0
        l = 0
        s_win = 0
        if s == x:
            return n
        for r in range(n):
            s_win+=nums[r]
            if s_win<s-x:
                continue
            elif s_win == s-x:
                length = max(length,r-l+1)
            elif s_win>s-x :
                while s_win>s-x and l<n:
                    s_win-=nums[l]
                    l+=1
                if s_win == s-x:
                    length = max(length,r-l+1)

        return n-length if length!= 0 else -1
