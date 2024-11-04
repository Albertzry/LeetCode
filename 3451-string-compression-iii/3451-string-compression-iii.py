class Solution(object):
    def compressedString(self, word):
        """
        :type word: str
        :rtype: str
        """
        t = []
        i0 = -1
        for i, c in enumerate(word):
            if i + 1 == len(word) or c != word[i + 1]:
                k, rem = divmod(i - i0, 9)
                t.append(("9" + c) * k)
                if rem:
                    t.append(str(rem))
                    t.append(c)
                i0 = i
        return ''.join(t)
