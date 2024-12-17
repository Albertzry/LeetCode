class Solution(object):
    def repeatLimitedString(self, s, repeatLimit):
        """
        :type s: str
        :type repeatLimit: int
        :rtype: str
        """
        from collections import Counter
        map = Counter(s)
        key = list(map.keys())
        key.sort(reverse=True)
        ans = []
        rc = 0
        while True:
            if rc < repeatLimit:
                ans.append(key[0])
                rc += 1
                map[key[0]] -= 1
                if map[key[0]] == 0:
                    key.pop(0)
                    rc = 0
            else:
                ans.append(key[1])
                map[key[1]] -= 1
                if map[key[1]] == 0:
                    key.pop(1)
                rc = 0
            if len(key) == 0 or len(key) == 1 and rc==repeatLimit:
                break
        return ''.join(ans)
                
                    