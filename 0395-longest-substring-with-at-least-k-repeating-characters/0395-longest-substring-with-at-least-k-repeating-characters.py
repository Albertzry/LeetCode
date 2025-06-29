class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        ln = len(s)
        cnt = Counter(s)
        goods = set()        
        for key, val in cnt.items():
            if val>= k:
                goods.add(key)
        if not goods:
            return 0
        dc = defaultdict(int)
        l = 0
        res = 0
        for r, sym in enumerate(s):
            if sym not in goods:
                l = r+1
                dc.clear()
            else:
                dc[sym]+=1
                if dc[sym] >= k:
                    temp_l = l
                    temp_dc = dc.copy()
                    while temp_dc[sym] >=k and not all(val >= k for val in temp_dc.values()):
                        sym1 = s[temp_l]
                        temp_l +=1
                        temp_dc[sym1]-=1
                        if temp_dc[sym1] == 0:
                            del temp_dc[sym1]
                    if temp_dc[sym] >=k:
                        res = max(res, r-temp_l+1)
        return res



        

       
       



        