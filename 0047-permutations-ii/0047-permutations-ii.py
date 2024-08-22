class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        temp=[]
        path=[]
        def backtracking(temp):
            if len(temp)==len(nums):
                if temp not in result:
                    result.append(temp[:])
                return
            for i in range(len(nums)):
                if i not in path:
                    temp.append(nums[i])
                    path.append(i)
                else:
                    continue
                backtracking(temp)
                temp.pop()
                path.pop()
            return
        backtracking(temp)
        return sorted(result)
