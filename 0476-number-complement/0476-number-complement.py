class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        num=list(str(bin(num))[2:])
        for i in range(len(num)):
            num[i]="1" if num[i]=="0" else "0"
        return int(''.join(num),2)