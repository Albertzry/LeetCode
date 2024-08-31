class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        cnt_a = 0
        cnt_b = 0
        res = 0

        for c in s:
            if c == 'b':
                if x >= y and cnt_a > 0:
                    res += x
                    cnt_a -= 1
                else:
                    cnt_b += 1
            elif c == 'a':
                if y > x and cnt_b > 0: 
                    res += y
                    cnt_b -= 1
                else:
                    cnt_a += 1
            else:  
                if cnt_a > 0 and cnt_b > 0:
                    res += min(x, y) * min(cnt_a, cnt_b)
                cnt_a = 0
                cnt_b = 0

        if cnt_a and cnt_b:
            res += min(x, y) * min(cnt_a, cnt_b)

        return res
        
