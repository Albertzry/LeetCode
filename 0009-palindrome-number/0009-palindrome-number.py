class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x=str(x)
        n=len(x)
        t=1
        for i in range(n//2):
            if x[i]!=x[n-i-1]:
                t=0
        if t==1:
            return True
        else :
            return False

