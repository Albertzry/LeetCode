class Solution:
    def concatenatedBinary(self, n: int) -> int:
        sum = ""
        for i in range(1,n+1):
            sum += bin(i)[2:]
        return int(sum,2) % (10**9 +7)