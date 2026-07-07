class Solution:
    def sumAndMultiply(self, n: int) -> int:
        nums = list(map(int,str(n)))
        sum = 0
        x = ''
        for num in nums:
            if num:
                sum+=num
                x+=str(num)
        return sum*int(x) if x else 0