class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = defaultdict(int)
        res = -1
        for i in nums:
            digitsSum = sum(int(c) for c in str(i))
            if digitsSum in d:
                res = max(res, d[digitsSum] + i)
                d[digitsSum] = max(d[digitsSum], i)
            else:
                d[digitsSum] = i
        return res
