class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []
        for row in grid:
            nums+=row
        nums.sort()
        n = len(nums)
        rm = nums[0]%x
        for num in nums:
            if num%x != rm:
                return -1
        target = nums[int(n/2)]
        ans = 0
        for num in nums:
            ans+=(abs(target-num))/x
        return int(ans)