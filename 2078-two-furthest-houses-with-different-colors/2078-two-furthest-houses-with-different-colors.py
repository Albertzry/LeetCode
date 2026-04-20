class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        l,r = 0,n-1
        dis = 0
        while l<n:
            r=n-1
            while r>=0:
                if colors[r]!=colors[l]:
                    dis = max(dis,r-l)
                    break
                r-=1
            l+=1
        return dis
