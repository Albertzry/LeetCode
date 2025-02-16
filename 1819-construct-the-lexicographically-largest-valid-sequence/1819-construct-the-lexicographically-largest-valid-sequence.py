class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = [0 for _ in range(2 * n - 1)]
        visited = [False for _ in range(n + 1)]
        
        def backtrace(i: int) -> bool:
            if i >= 2 * n - 1:
                return True
            if res[i] != 0:
                return backtrace(i + 1)
            for x in range(n, 0, -1):
                if visited[x] == True:
                    continue
                if x == 1:       
                    visited[1] = True       
                    res[i] = 1              
                    if backtrace(i + 1) == True:
                        return True
                    res[i] = 0             
                    visited[1] = False      
                else:
                    if i + x >= 2 * n - 1:
                        continue
                    if res[i] != 0 or res[i + x] != 0:
                        continue
                    res[i] = x             
                    res[i + x] = x          
                    visited[x] = True      
                    if backtrace(i + 1) == True:
                        return True
                    visited[x] = False      
                    res[i + x] = 0          
                    res[i] = 0              
            return False
        
        backtrace(0)
        return res
