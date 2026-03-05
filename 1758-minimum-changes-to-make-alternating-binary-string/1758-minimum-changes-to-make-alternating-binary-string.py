class Solution:
    def minOperations(self, s: str) -> int:
        a,b = 0,0
        for i,l in enumerate(s):
            if i%2 == 0:
                if l == '1':
                    a+=1
                else:
                    b+=1
            else:
                if l == '0':
                    a+=1
                else:
                    b+=1
        return min(a,b)