class Solution:
    def longestBalanced(self, s: str) -> int:
        l = len(s)
        ans = 0
        bf,bf_p = s[0],0
        for i,lt in enumerate(s):
            if lt!= bf:
                bf = lt
                bf_p = i
            else:
                ans = max(ans,i-bf_p+1)
        
        ans = max(ans,self.two(s,'a','b','c'))
        ans = max(ans,self.two(s,'a','c','b'))
        ans = max(ans,self.two(s,'b','c','a'))
        ans = max(ans,self.three(s))
        return ans
    

    def two(self,s,letter1,letter2,target):
        ans = 0
        rc = defaultdict(list)
        rc[0].append(0)
        r = 0
        for i,lt in enumerate(s):
            if lt == target:
                for key in rc:
                    ans = max(ans,rc[key][-1]-rc[key][0])
                rc.clear()
                rc[0].append(i+1)
                r=0
            else:
                if lt == letter1:
                    r+=1
                else:
                    r-=1
                rc[r].append(i+1)
        for key in rc:
            ans = max(ans,rc[key][-1]-rc[key][0])
        return ans

    def three(self,s):
        ans = 0
        r1,r2=0,0
        rc = defaultdict(list)
        rc[(0,0)].append(0)
        for i , lt in enumerate(s):
            if lt == 'a':
                r1+=1
            elif lt == 'b':
                r1-=1
                r2+=1
            else:
                r2-=1
            rc[(r1,r2)].append(i+1)
        for key in rc:
            ans = max(ans,rc[key][-1]-rc[key][0])
        return ans


        

