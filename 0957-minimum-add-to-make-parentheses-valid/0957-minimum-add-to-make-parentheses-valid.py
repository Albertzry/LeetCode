class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        cnt = 0
        for c in s:
            if c=="(":
                stack.append(c)
                continue
            if stack :
                stack.pop(-1)
            else:
                cnt+=1
        return cnt+len(stack)