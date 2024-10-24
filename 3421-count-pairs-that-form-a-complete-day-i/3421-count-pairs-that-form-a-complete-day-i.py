class Solution(object):
    def countCompleteDayPairs(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        from collections import defaultdict
        map = defaultdict(list)
        for i,hour in enumerate(hours):
            map[hour%24].append(i)
        ans=0
        for key in map:
            temp = 24-key
            if key == 0 or key == 12:
                ans+=len(map[key])*(len(map[key])-1)/2
            elif map[key] and temp in map:
                    ans+=len(map[key])*len(map[temp])
                    map[key]=None
                    map[temp]=None
        return ans
                
            