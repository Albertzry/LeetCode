class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        n_1 = cnt[1]
        ans = n_1 if n_1 %2 == 1 else n_1 -1

        for num in nums:
            if num == 1:
                continue
            i = 0
            while True:
                if cnt[num**(2**i)] >= 2:
                    i+=1
                    continue
                elif cnt[num**(2**i)] == 1:
                    i+=1
                    break
                elif cnt[num**(2**i)] == 0:
                    break
            ans = max(ans, 2*i -1)
        return ans