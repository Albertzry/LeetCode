class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ex = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        n = len(s)
        result = 0
        i = 0
        while i < n:
            if i < n - 1:
                if ex[s[i]] < ex[s[i + 1]]:
                    result += ex[s[i + 1]]
                    result -= ex[s[i]]
                    i+=2
                else:
                    result += ex[s[i]]
                    i+=1
            else:
                result += ex[s[i]]
                i+=1
        return result