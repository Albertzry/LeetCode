class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        s=list(s)
        goal=list(goal)
        i,n=0,len(s)
        while i<n:
            if s==goal:
                return True
            temp=s.pop(0)
            s.append(temp)
            i+=1
        return False