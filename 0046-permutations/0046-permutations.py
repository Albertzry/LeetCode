class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        temp=[]
        def backtracking(temp):
            if len(temp)==len(nums):
                result.append(temp[:])
                return
            for i in range(len(nums)):
                if nums[i] not in temp:
                    temp.append(nums[i])
                else:
                    continue
                backtracking(temp)
                temp.pop()
            return
        backtracking(temp)
        return sorted(result)