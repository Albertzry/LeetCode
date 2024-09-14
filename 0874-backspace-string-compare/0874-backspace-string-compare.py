class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def backspace(string):
            if string.count("#")==0:
                return string
            else:
                temp=[]
                for ch in string:
                    if temp and ch=="#":
                        temp.pop(-1)
                    elif ch!="#":
                        temp.append(ch)
                return ''.join(temp)
        return backspace(s)==backspace(t)