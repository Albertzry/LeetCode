class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = list(str(num))
        n = len(num)
        i=0
        while i <n:
            temp = max(num[i:])
            if num[i]==temp:
                i+=1
                continue
            else:
                j=-1
                while num[j]!=temp:
                    j-=1
                num[j]=num[i]
                num[i]=temp
                break
        return int("".join(num))
