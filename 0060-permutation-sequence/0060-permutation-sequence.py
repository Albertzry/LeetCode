class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import itertools
        nums = []
        for i in range(n):
            nums.append(i+1)
        temp = list(itertools.permutations(nums))
        return ''.join(map(str, temp[k-1]))