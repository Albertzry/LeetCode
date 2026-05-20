class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        s1,s2 = set(),set()
        ans = []
        for i in range(len(A)):
            s1.add(A[i])
            s2.add(B[i])
            ans.append(len(s1&s2))
        return ans