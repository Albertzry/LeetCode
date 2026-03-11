class Solution:
    def bitwiseComplement(self, n: int) -> int:
        num = bin(n)[2:]
        ans=''
        for i in num:
            if i == '0':
                ans+='1'
            else:
                ans+='0'
        return int(ans,2)