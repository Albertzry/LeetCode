class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        s="0"
        j=0
        while j<n:
            temp=list(s[:])
            s+="1"
            for i in range(len(temp)):
                if temp[i]=="0":
                    temp[i]="1"
                elif temp[i]=="1":
                    temp[i]="0"
            temp.reverse()
            s+="".join(temp)
            j+=1
        return s[k-1]