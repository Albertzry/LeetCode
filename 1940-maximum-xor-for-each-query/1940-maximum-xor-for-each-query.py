class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        n = len(nums)
        mask = (1 << maximumBit) - 1
        xorsum = reduce(xor, nums)

        ans = list()
        for i in range(n - 1, -1, -1):
            ans.append(xorsum ^ mask)
            xorsum ^= nums[i]

        return ans
        