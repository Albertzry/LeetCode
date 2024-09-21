class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        nums = [i+1 for i in range(n)]
        nums = list(map(str,nums))
        nums.sort()
        nums= list(map(int,nums))
        return nums