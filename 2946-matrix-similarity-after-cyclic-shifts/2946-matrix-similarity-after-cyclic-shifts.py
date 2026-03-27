class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m,n = len(mat), len(mat[0])
        for i in range(m):
            shift = -k if n%2 == 0 else k
            for j in range(n):
                if j+shift>=0 and j+shift <n:
                    if mat[i][j+shift] != mat[i][j]:
                        return False
                else:
                    if mat[i][j-(k%n)]!= mat[i][j]:
                        return False
        return True 
                    