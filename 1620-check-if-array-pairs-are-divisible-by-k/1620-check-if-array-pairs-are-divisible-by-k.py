class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        mod = [0] * k
        for num in arr:
            mod[num % k] += 1
        if any(mod[i] != mod[k - i] for i in range(1, k // 2 + 1)):
            return False
        return mod[0] % 2 == 0
