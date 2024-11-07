class Solution(object):
    def losingPlayer(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: str
        """
        cnt=-1
        while True:
            x-=1
            y-=4
            cnt+=1
            if x<0 or y<0:
                break
        if cnt%2==0:
            return "Bob"
        else:
            return "Alice"   