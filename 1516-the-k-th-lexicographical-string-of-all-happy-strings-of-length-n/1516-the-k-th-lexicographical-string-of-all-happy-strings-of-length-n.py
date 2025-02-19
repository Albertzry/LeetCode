class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 << (n - 1): # 3 * 2 ** (n - 1)
            return ''
        
        ans = ['x']
        k -= 1
        n = 1 << (n - 1)
        while n:
            order = k // n
            ans.append([x for x in 'abc' if x != ans[-1]][order])
            k %= n
            n >>= 1
        return ''.join(ans[1: ])
