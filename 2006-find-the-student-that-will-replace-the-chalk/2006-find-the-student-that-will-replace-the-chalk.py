class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        chalk_sum=sum(chalk)
        remainder=k%chalk_sum
        n=0
        for i in range(len(chalk)):
            n+=chalk[i]
            if n >remainder:
                return i