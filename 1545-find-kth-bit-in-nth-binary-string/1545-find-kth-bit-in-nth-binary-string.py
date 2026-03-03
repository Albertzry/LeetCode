class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = '0'
        for i in range(2,n+1):
            temp = ''
            for l in s:
                temp += '0' if l == '1' else '1'
            s += '1'
            for i in range(len(temp)-1,-1,-1):
                s+=temp[i]
        return s[k-1]