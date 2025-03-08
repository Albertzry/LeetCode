class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        wd=[]
        n=len(blocks)
        cnt=0
        ans=n
        for i in range(n):
            if len(wd)<k-1:
                wd.append(blocks[i])
                cnt+=(blocks[i]=='W')
            elif len(wd)==k-1:
                wd.append(blocks[i])
                cnt+=(blocks[i]=='W')
                ans=min(ans,cnt)
            else:
                cnt-=(wd[0]=='W')
                cnt+=(blocks[i]=='W')
                wd.pop(0)
                wd.append(blocks[i])
                ans=min(ans,cnt)
        return ans

            
            