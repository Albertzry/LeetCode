class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        cnt = [0,0,0]
        i,j=0,0
        while i <n:
            while 0 in cnt and j<n:
                if s[j] == 'a':
                    cnt[0]+=1
                elif s[j] == 'b':
                    cnt[1]+=1
                elif s[j] == 'c':
                    cnt[2]+=1
                j+=1
            if 0 not in cnt:
                ans += n-j+1
            if s[i] == 'a':
                cnt[0]-=1
            elif s[i] == 'b':
                cnt[1]-=1
            elif s[i] == 'c':
                cnt[2]-=1
            i+=1
            

        return ans