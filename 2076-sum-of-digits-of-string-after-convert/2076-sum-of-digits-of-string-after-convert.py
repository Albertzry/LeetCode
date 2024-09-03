class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        temp=""
        for i in range(len(s)):
            temp+=''.join(str(ord(s[i])-ord('a')+1))
        result = 0
        while k!=0:
            result = 0
            for i in range(len(temp)):
                result+=int(temp[i])
            temp = str(result)
            k-=1
        return result
        