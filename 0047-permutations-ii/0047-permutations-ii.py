class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        temp=[]
        def backtracking(current,temp):
            if len(temp)==len(nums):
                if temp not in result:
                    result.append(temp[:])
                return
            for i in range(current+1,len(nums)):
                temp.append(nums[i])
                backtracking(i,temp)
                temp.pop()
            return
        backtracking(0,temp)
        return sorted(result)