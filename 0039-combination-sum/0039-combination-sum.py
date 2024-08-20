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
#下面是另外一种回溯，不用pop
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def find(s, use, remain):    #s表示起始起始位置，use表示已经添加的数列，remain表示剩余
            for i in range(s, len(candidates)):
                c = candidates[i]
                if c == remain:
                    ans.append(use + [c])
                    return
                if c < remain:
                    find(i, use + [c], remain - c)
                if c > remain:
                    return
        find(0, [], target)
        return ans

            
