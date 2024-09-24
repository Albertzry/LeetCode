class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        prefix = set()
        for num in arr1:
            while num and num not in prefix:
                prefix.add(num)
                num//=10
        ans = -1
        for num in arr2:
            while num:
                if num in prefix:
                    ans=max(ans,num)
                    break
                num//=10
        return 0 if ans == -1 else len(str(ans))
        
