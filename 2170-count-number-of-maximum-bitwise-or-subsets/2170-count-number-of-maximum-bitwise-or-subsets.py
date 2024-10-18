class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        map = defaultdict(list)

        def backtrack(current,remainder,map):
            if current:
                temp = current[0]
                for num in current:
                    temp|=num
                map[temp].append(current)
            if not remainder:
                return
            for i,num in enumerate(remainder):
                current.append(num)
                if i<len(remainder)-1:
                    backtrack(current,remainder[i+1:],map)
                elif i==len(remainder)-1:
                    backtrack(current,[],map)
                current.pop(-1)
            return
        
        re = nums[:]
        backtrack([],re,map)
        max_res=max(map.keys())
        return len(map[max_res])
        