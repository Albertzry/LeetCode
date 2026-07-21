class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ans = s.count('1')
        n = len(s)
        l = []
        i = 0
        while i <n:
            now,pos = s[i], i
            while i+1<n and s[i+1] ==now :
                i+=1
            i+=1
            l.append([now,i-pos])
            
        
        m = len(l)
        plus = 0
        for i in range(1,m-1):
            if l[i-1][0] == '0' and l[i+1][0] =='0':
                plus = max(plus,l[i-1][1]+l[i+1][1])
        return ans+plus