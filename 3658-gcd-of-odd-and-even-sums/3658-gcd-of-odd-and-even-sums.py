class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        o = n**2
        e = n*(n+1)
        ans = ceil(sqrt(o))
        while True:
            if o%ans == 0 and e%ans ==0:
                return ans
            else:
                ans-=1