class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1_o, s1_e = [], []
        s2_o, s2_e = [], []
        for i in range(n):
            if i % 2 == 0:
                s1_e.append(s1[i])
                s2_e.append(s2[i])
            else:
                s1_o.append(s1[i])
                s2_o.append(s2[i])
        s1_e.sort()
        s1_o.sort()
        s2_e.sort()
        s2_o.sort()
        return s1_o == s2_o and s1_e ==s2_e
    