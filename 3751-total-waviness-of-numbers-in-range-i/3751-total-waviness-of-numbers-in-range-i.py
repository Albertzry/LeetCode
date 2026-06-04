class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        ans = 0
        for num in range(num1,num2+1):
            nl = list(map(int,list(str(num))))
            n = len(nl)
            for i in range(1,n-1):
                if nl[i]>nl[i-1] and nl[i]>nl[i+1]:
                    ans +=1
                elif nl[i]<nl[i-1] and nl[i]<nl[i+1]:
                    ans +=1
        return ans
            