class Solution:
    def minEnd(self, n: int, x: int) -> int:
        bitCount = n.bit_length() + x.bit_count()
        res, j = x, 0
        m = n - 1
        for i in range(bitCount):
            if ((res >> i) & 1) == 0:
                if ((m >> j) & 1) != 0:
                    res |= (1 << i)
                j += 1
        return res
