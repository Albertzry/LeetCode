class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ll = len(str(low))
        lh = len(str(high))
        s = str(low)[0]
        e = str(high)[0]
        ans = []
        for i in range(ll,lh+1):
            if i == ll:
                for num in range(int(s),10):
                    temp = 0
                    tn = num
                    for j in range(ll):
                        temp*=10
                        temp+=tn
                        tn+=1
                        if tn >9:
                            break
                    if len(str(temp)) == ll and temp <= high and temp >=low:
                        ans.append(temp)
            elif i == lh:
                for num in range(1,int(e)+1):
                    temp = 0
                    tn = num
                    for j in range(lh):
                        temp*=10
                        temp+=tn
                        tn+=1
                        if tn >9:
                            break
                    if len(str(temp)) == lh and temp <= high and temp >=low:
                        ans.append(temp)
            else:
                for num in range(1,10):
                    temp = 0
                    tn = num
                    for j in range(i):
                        temp*=10
                        temp+=tn
                        tn+=1
                        if tn >9:
                            break
                    if len(str(temp)) == i:
                        ans.append(temp)
        return ans
        