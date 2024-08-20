class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans = []
        def find(s,use,remain):
            for i in range(s,len(candidates)):
                c = candidates[i]
                if i>s and candidates[i-1]==candidates[i]:
                    continue
                if c == remain:
                    ans.append(use + [c])
                    return              
                if c < remain:
                    find(i+1,use + [c], remain - c)
                if c > remain:
                    return
        find(0,[], target)
        return ans

