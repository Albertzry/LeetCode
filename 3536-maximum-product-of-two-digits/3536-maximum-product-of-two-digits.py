class Solution:
    def maxProduct(self, n: int) -> int:
        l = list(map(int,str(n)))
        l.sort()
        return l[-1]*l[-2]