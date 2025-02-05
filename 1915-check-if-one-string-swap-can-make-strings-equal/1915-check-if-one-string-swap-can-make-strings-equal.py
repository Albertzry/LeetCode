class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        i = j = -1
        for idx, (x, y) in enumerate(zip(s1, s2)):
            if x != y:
                if i < 0:
                    i = idx
                elif j < 0:
                    j = idx
                else:
                    return False
        return i < 0 or j >= 0 and s1[i] == s2[j] and s1[j] == s2[i]
