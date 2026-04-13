class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ans = 10**4
        for i,num in enumerate(nums):
            if num == target:
                ans = min(ans,abs(i-start))
                if i >= start+ans:
                    break
        return ans