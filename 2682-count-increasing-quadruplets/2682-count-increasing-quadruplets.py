class Solution(object):
    def countQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        less = [0] * (n + 1)
        ans = 0
        for j in range(1, n - 1):
            for x in range(nums[j - 1] + 1, n + 1):
                less[x] += 1

            great = 0  
            for k in range(n - 1, j, -1):
                if nums[k] < nums[j]:
                    ans += less[nums[k]] * great
                else:  
                    great += 1
        return ans

        