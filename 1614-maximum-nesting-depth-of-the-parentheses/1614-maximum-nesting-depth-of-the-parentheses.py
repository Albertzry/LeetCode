class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        cnt = 0
        st = []
        for ch in s:
            if ch == '(':
                cnt+=1
                st.append('(')
            if ch == ')':
                ans = max(ans,cnt)
                st.pop()
                cnt-=1
        return ans