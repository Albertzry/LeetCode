class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        vals = {int(num, 2) for num in nums}
        val = 0
        while val in vals:
            val += 1
        res = "{:b}".format(val)
        return '0' * (n - len(res)) + res
