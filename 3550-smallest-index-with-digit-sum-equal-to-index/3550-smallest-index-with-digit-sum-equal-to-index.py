class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i,num in enumerate(nums):
            if i == sum(list(map(int,str(num)))):
                return i
        return -1