class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n%3!=2 and n!=1:
            if n%3==1:
                n-=1
            else:
                n/=3
        if n%3==2:
            return False
        else:
            return True
        