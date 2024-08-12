class Solution(object):
   
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        max_str=""
        def judge(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        for i in range(len(s)):
            str1 = judge(i,i)
            str2 = judge(i,i+1)
            max_str = str1 if len(str1) > len(max_str) else max_str
            max_str = str2 if len(str2) > len(max_str) else max_str

        return max_str
