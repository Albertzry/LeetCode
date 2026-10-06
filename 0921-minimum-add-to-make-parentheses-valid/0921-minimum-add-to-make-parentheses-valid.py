class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = []
        for c in s:
            if c == '(':
                st.append('(')
            else:
                if st and st[-1] == '(':
                    st.pop()
                else:
                    st.append(')')
        return len(st)