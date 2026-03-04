class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m,n = len(mat),len(mat[0])
        ans = 0
        rc = []
        for row in mat:
            if sum(row) == 1:
                rc.append(1)
            else:
                rc.append(0)

        for i,r in enumerate(rc):
            if r ==1 :
                for j in range(n):
                    if mat[i][j] == 1:
                        sum_c = 0
                        for k in range(m):
                            sum_c += mat[k][j]
                        if sum_c == 1:
                            ans+=1
        return ans
            