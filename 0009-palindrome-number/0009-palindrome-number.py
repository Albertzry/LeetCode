class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        reverse_x = str_x[::-1]
        return str_x == reverse_x

