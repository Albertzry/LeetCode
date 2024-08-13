class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0 or s.count(" ")==len(s):
            return 0
        j=0
        while s[j]==" ":
            j+=1
        s=s[j:]
        if (ord(s[0]) < ord("0") or ord(s[0]) > ord("9")) and s[0] != "-" and s[0] != "+":
            return 0
        t=1
        i=0
        if s[0] == "+":
            t = 1
            i=1
        if s[0] == "-":
            t = 0
            i=1
        result = 0
        while i<len(s) and ord(s[i])>=ord("0") and ord(s[i])<=ord("9") :
            result = result * 10 + int(s[i])
            i += 1
        if t ==1:
            if result > -1+2**31:
                return -1+2**31
            else:
                return result
        if t==0:
            if -result <-(2**31):
                return -(2**31)
            else:
                return -result