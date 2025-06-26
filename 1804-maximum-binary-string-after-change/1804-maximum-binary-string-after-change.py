class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        n = len(binary)
        z = binary.count('0')
        
        if z < 2:
            return binary
        
        first_zero = binary.find('0')
        p = first_zero + z - 1
        
        return '1' * p + '0' + '1' * (n - p - 1)
        