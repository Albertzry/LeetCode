class Solution(object):
    def minExtraChar(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        n = len(s)
        d = [-1] * (n + 1)
        d[0] = 0
        mp = dict()
        for e in dictionary:
            mp[e] = mp[e] + 1 if e in mp else 1
        for i in range (1, n + 1):
            d[i] = d[i - 1] + 1
            for j in range(i - 1, -1, -1):
                if s[j:i] in mp:
                    d[i] = min(d[i], d[j])
        return d[n]
