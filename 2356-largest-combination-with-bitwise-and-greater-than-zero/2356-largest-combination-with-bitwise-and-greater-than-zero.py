class Solution(object):
    def largestCombination(self, candidates):
        """
        :type candidates: List[int]
        :rtype: int
        """
        from collections import defaultdict
        map=defaultdict(list)
        for i,num in enumerate(candidates):
            num=str(bin(num))[2:]
            for j in range(-1,-len(num) - 1, -1):
                if num[j]=='1':
                    map[-j-1].append(i)
        ans=0
        for key in map:
            ans=max(ans,len(map[key]))
        return ans