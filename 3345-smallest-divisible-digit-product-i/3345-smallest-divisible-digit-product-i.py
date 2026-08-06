class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            temp = list(map(int,str(n)))
            num = temp[0]
            for i in range(1,len(temp)):
                num*=temp[i]
            if num%t ==0:
                return n
            n+=1