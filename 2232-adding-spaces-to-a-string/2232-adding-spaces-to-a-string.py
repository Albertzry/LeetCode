class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        ans=[]
        i=0
        n=len(spaces)
        ans.append(s[:spaces[0]])
        ans.append(' ')
        for i in range(1,n):
            ans.append(s[spaces[i-1]:spaces[i]])
            ans.append(' ')
        ans.append(s[spaces[n-1]:])
        return "".join(ans)