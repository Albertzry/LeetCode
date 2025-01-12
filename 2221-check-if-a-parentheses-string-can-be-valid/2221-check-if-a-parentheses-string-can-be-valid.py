class Solution(object):
    def canBeValid(self, s, locked):
        """
        :type s: str
        :type locked: str
        :rtype: bool
        """
        n = len(s)
        mx = 0  
        mn = 0   
        for i in range(n):
            if locked[i] == '1':
                if s[i] == '(':
                    diff = 1
                else:
                    diff = -1
                mx += diff
                mn = max(mn + diff, (i + 1) % 2)
            else:
                mx += 1
                mn = max(mn - 1, (i + 1) % 2)
            if mx < mn:
                return False
        return mn == 0

            