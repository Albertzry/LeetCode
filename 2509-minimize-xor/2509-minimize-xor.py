class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        c1 = num1.bit_count()
        c2 = num2.bit_count()
        while c2 < c1:
            num1 &= num1 - 1  
            c2 += 1
        while c2 > c1:
            num1 |= num1 + 1  
            c2 -= 1
        return num1
