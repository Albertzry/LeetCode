class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        return all(x % 2 != y % 2 for x, y in pairwise(nums))