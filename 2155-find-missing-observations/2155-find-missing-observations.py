class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """
        remainder = (len(rolls)+n)*mean - sum(rolls)
        if 1*n >remainder or 6*n <remainder:
            return []
        if remainder % n ==0:
            return [remainder//n]*n
        else:
            result=[]
            while remainder!=0:
                result.append(remainder//n)
                remainder-=remainder//n
                n-=1
            return result