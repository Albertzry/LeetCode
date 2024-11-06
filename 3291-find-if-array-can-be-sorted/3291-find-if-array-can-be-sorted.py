class Solution(object):
    def canSortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i, n = 0, len(nums)
        pre_max = 0
        c = str(bin(nums[0])).count("1")
        while i < n:
            temp = []
            while i<n and str(bin(nums[i])).count("1") == c:
                temp.append(nums[i])
                i+=1
            if min(temp) < pre_max:
                return False
            pre_max = max(temp)
            if i < n:
                c = str(bin(nums[i])).count("1")
        return True
            
        