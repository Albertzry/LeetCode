class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        suffix_sum = [0] * (n - 1) + [stoneValue[-1]]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + stoneValue[i]
    
        f = [0] * n + [0]
        for i in range(n - 1, -1, -1):
            f[i] = suffix_sum[i] - min(f[i+1:i+4])
        
        total = sum(stoneValue)
        if f[0] * 2 == total:
            return "Tie"
        else:
            return "Alice" if f[0] * 2 > total else "Bob"