class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        s = ['a'] * (n + m - 1)
        fixed = [False] * (n + m - 1)
        
        # 处理 'T' 的情况
        for i, ch in enumerate(str1):
            if ch == 'T':
                for j, c in enumerate(str2, i):
                    if fixed[j] and s[j] != c:
                        return ""
                    s[j], fixed[j] = c, True
        
        for i, ch in enumerate(str1):
            if ch == 'F':
                if any(str2[j-i] != s[j] for j in range(i, i+m)):
                    continue
                
                # 找第一个可修改的位置
                for j in range(i+m-1, i-1, -1):
                    if not fixed[j]:
                        s[j] = 'b'
                        break
                else:
                    return ""
        
        return ''.join(s)
