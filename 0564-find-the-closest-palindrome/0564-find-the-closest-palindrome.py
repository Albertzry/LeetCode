class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        if len(n) == 1:
            return str(int(n) - 1)
        length = len(n)
        i = 0
        if length % 2 == 0:
            num1=n[:length // 2] + n[length // 2-1::-1]
            temp2=str(int(n[:length // 2])+1)
            num2=temp2+temp2[length//2-1::-1]
            temp3 = str(int(n[:length // 2]) - 1)
            num3 = temp3 + temp3[length // 2 - 1::-1]

        else:
            num1=n[:1+length // 2] + n[length//2-1::-1]
            temp2=str(int(n[:1+length // 2])+1)
            num2=temp2+temp2[length//2-1::-1]
            temp3 = str(int(n[:1 + length // 2]) - 1)
            num3 = temp3 + temp3[length // 2 - 1::-1]
        if num1 == n:
            if length % 2 == 0:
                temp1 = str(int(n[:length // 2]) - 1)
                num1 = temp1 + temp1[::-1]
            else:
                temp1=str(int(n[:1+length // 2]) - 1)
                num1 = temp1 + temp1[:-1][::-1]
        num4=(length-1)*"9"
        return min([num1,num2,num3,num4],key=lambda x:(abs(int(x)-int(n)),int(x)))