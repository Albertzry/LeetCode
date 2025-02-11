class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        m = len(part)
        res = ""
        for ch in s:
            res += ch
            if len(res) >= m and res[-m:] == part:
                res = res[:-m]
        return res

