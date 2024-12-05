class Solution(object):
    def canMakeSubsequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        if len(str1) < len(str2):
            return False
        j = 0
        for b in str1:
            c = chr(ord(b) + 1) if b != 'z' else 'a'
            if b == str2[j] or c == str2[j]:
                j += 1
                if j == len(str2):
                    return True
        return False
