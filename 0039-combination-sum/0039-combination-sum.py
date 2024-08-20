class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(start, temp):
            if sum(temp) == target:
                result.append(temp[:])
                return
            if sum(temp) > target:
                return
            for i in range(start, len(candidates)):
                temp.append(candidates[i])
                backtrack(i, temp)
                temp.pop()
        result = []
        temp = []
        backtrack(0, temp)
        return result
            
            