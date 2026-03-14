class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def trace_back(record,now,n):
            flag = False
            for l in 'abc':
                if not now or l != now[-1]:
                    if len(now) == n-1:
                        heapq.heappush(record,now+l)
                        flag = True
                    else:
                        trace_back(record,now+l,n)
            if flag:
                return
        pq = []
        trace_back(pq,'',n)
        if len(pq) < k:
            return ""
        else:
            return pq[k-1]

        
        

