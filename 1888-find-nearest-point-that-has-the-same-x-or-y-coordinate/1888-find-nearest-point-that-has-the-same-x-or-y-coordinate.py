class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        res=-1
        min_=float('inf')
        for i, (x1,y1) in enumerate(points):
            if x1==x or y1==y:
                if abs(x1 - x) + abs(y1 - y)<min_:
                    min_=abs(x1 - x) + abs(y1 - y)
                    res=i
        return res
            