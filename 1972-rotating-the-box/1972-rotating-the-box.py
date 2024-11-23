class Solution(object):
    def rotateTheBox(self, box):
        """
        :type box: List[List[str]]
        :rtype: List[List[str]]
        """
        m, n = len(box), len(box[0])
        ans = [['.'for _ in range(m)] for _ in range(n)]
        for i in range(m):
            r = 0
            while r < n:
                cnt = 0
                while r<n and box[i][r] != '*':
                    if box[i][r] == '#':
                        cnt += 1
                    r += 1
                if r<n:
                    ans[r][m-i-1] = '*'
                l = 1
                while l <= cnt:
                    ans[r-l][m-i-1] = '#'
                    l += 1
                r += 1
        return ans
                        
                            
                    