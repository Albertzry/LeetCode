class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        vowel={'a','e','i','o','u'}
        judge=[0]
        for i,word in enumerate(words):
            if word[0] in vowel and word[-1] in vowel:
                judge.append(judge[i]+1)
            else:
                judge.append(judge[i])
        ans=[]
        for query in queries:
            ans.append(judge[query[1]+1]-judge[query[0]])
        return ans