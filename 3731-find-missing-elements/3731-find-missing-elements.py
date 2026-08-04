class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        a,b = min(nums),max(nums)
        nums = set(nums)
        ans = []
        for i in range(a,b):
            if i not in nums:
                ans.append(i)
        return ans
