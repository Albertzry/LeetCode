class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans_bin = ''
        for i in range(1,n+1):
            ans_bin+=bin(i)[2:]
        return int(ans_bin,2)%(10**9+7)