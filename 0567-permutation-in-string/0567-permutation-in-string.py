class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        freq1 = [0] * 26
        freq2 = [0] * 26

        for i in range(n1):
            freq1[ord(s1[i]) - ord("a")] += 1
            freq2[ord(s2[i]) - ord("a")] += 1

        if freq1 == freq2:
            return True

        for i in range(n1, n2):
            freq2[ord(s2[i]) - ord("a")] += 1
            freq2[ord(s2[i - n1]) - ord("a")] -= 1
            if freq1 == freq2:
                return True
        return False