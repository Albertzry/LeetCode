class Solution:
    def checkValidString(self, s: str) -> bool:
        mn = mx = 0  # 未匹配的左括号的个数的最小值和最大值

        for ch in s:
            if ch == '(':
                mn += 1
                mx += 1
            elif ch == ')':
                mn -= 1
                mx -= 1
                if mx < 0:  # 右括号太多了
                    return False
            else:  # '*'
                mn -= 1  # '*' 改成右括号
                mx += 1  # '*' 改成左括号
            mn = max(mn, 0)  # 未匹配的左括号的个数不能为负

        return mn == 0  
