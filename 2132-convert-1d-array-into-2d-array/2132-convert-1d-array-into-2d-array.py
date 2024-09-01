class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        if len(original)!=m*n:
            return []
        result=[]
        i=0
        while i<len(original):
            result.append(original[i:i+n])
            i+=n
        return result
            
