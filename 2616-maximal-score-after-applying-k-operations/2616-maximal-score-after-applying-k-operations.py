class Solution(object):
    def maxKelements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        nums = list(map(lambda x:x*-1,nums))
        nums.sort()
        i = 0
        ans = 0
        while i <k:
            temp = heapq.heappop(nums)
            ans += -temp
            temp //=3
            heapq.heappush(nums,temp)
            i+=1
        return ans