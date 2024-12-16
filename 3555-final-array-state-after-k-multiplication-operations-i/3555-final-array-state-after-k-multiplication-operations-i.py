class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        import heapq
        temp=[]
        n=len(nums)
        for i in range(n):
            heapq.heappush(temp,[nums[i],i])
        i=0
        while i<k:
            num,index=heapq.heappop(temp)
            heapq.heappush(temp,[num*multiplier,index])
            i+=1
        for num,index in temp:
            nums[index]=num
        return nums
        