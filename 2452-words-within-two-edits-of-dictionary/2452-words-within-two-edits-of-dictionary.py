class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        for word1 in queries:
            for word2 in dictionary:
                if self.find_dif(word1,word2):
                    ans.append(word1)
                    break
        return ans
        
    def find_dif(self,word1,word2):
        n = len(word1)
        cnt = 0
        for i in range(n):
            if word1[i]!=word2[i]:
                cnt+=1
            if cnt>2:
                return False
        return True