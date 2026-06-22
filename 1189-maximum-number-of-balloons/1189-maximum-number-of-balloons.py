class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        n_b = text.count('b')
        n_a = text.count('a')
        n_l = text.count('l')
        n_o = text.count('o')
        n_n = text.count('n')
        ans = 0
        for i in range(1,len(text)):
            if i<=n_b and i<=n_a and 2*i<=n_l and 2*i<=n_o and i<=n_n:
                ans+=1
            else:
                break
        return ans