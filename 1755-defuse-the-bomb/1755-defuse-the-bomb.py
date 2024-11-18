class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n=len(code)
        if k==0:
            return [0]*n
        code=code+code
        if k>0:
            for i in range(n):
                code[i]=sum(code[i+1:i+k+1])
            return code[0:n]
        if k<0:
            for i in range(2 * n-1,n-1,-1):
                code[i]=sum(code[i+k:i])
            return code[n:]