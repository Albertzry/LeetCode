class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        i,n=0,len(s)
        while i<n:
            if '0'<=s[i]<='9':
                s.pop(i)
                if i>0 and 'a'<=s[i-1]<='z':
                    s.pop(i-1)
                    i-=1
                n=len(s)
            else:
                i+=1
            
        return ''.join(s)
        