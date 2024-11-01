class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for ch in s:
            if len(stack)<2:
                stack.append(ch)
                continue
            if ch==stack[-1] and stack[-1]==stack[-2]:
                continue
            stack.append(ch)
        return ''.join(stack)