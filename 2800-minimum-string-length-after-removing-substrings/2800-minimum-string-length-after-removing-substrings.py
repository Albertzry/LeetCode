class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for letter in s:
            if not stack:
                stack.append(letter)
                continue
            if stack[-1]=='A' and letter=='B' or stack[-1]=='C' and letter=='D':
                stack.pop(-1)
                continue
            stack.append(letter)
        return len(stack)