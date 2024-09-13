class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        xors = [0]
        for num in arr:
            xors.append(xors[-1] ^ num)
        
        ans = list()
        for left, right in queries:
            ans.append(xors[left] ^ xors[right + 1])
        
        return ans