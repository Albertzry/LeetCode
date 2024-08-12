class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        row=dict()
        for i in range(numRows):
            row[i]=[]

        num =0
        t =1
        for i in range(len(s)):
            row[num].append(s[i])
            if t==1:
                num+=1
            else:
                num-=1
            if num == numRows:
                t = -1
                num -=2
            if num == -1:
                t = 1
                num += 2
        result=""
        for i in range(numRows):
             result +=''.join(row[i])
        return result
        