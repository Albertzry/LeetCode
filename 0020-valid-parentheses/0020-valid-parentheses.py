class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        def judge(b,a):
            if (a=="(" and b==")") or (a=="[" and b=="]") or (a=="{"and b=="}"):
                return True
            else:return False
        
        for i in range(len(s)):
            stack.append(s[i])
            if len(stack)>1 and judge(stack[len(stack)-1],stack[len(stack)-2]):
                stack.pop()
                stack.pop()
        return not stack
