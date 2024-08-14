class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        i=0
        j=0
        min_len = len(min(strs,key=len))
        if min_len==0:
            return ""
        while j < 200:
            temp = strs[0][j]
            t=1
            for i in range(len(strs)):
                if temp!=strs[i][j]:
                    t=0
            if t==1:
                result+=temp
            else:
                break
            i+=1
            j+=1
            if j==min_len:
                break
        return result


            
