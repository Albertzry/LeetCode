class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def calculate(time1,time2):
            ans=0
            ans +=(int(time2[0])-int(time1[0]))*600
            ans +=(int(time2[1])-int(time1[1]))*60
            ans +=(int(time2[3])-int(time1[3]))*10
            ans +=(int(time2[4])-int(time1[4]))
            return ans
        timePoints=sorted(timePoints)
        res=1440
        for i in range(len(timePoints)-1):
            if timePoints[i]==timePoints[i+1]:
                return 0
            res=min(res,calculate(timePoints[i],timePoints[i+1]))
        if timePoints[0]!=timePoints[-1]:
            temp = ''.join([str(int(timePoints[0][0:2])+24), ':',timePoints[0][3],timePoints[0][4]])
            res=min(res,calculate(timePoints[-1],temp))
        return res
        