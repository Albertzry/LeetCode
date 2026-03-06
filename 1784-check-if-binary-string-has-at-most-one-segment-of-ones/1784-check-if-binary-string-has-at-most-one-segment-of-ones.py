class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        ans = False
        flag = False
        for a in s:
            if a == '1':
                if flag == False:
                    flag = True
                    if ans == False:
                        ans = True
                    else:
                        return False
            else:
                flag = False
        return ans
            