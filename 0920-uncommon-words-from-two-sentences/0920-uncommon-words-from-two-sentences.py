class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        hashmap = dict()
        temp=[]
        for i in range(len(s1)):
            if s1[i] == " ":
                word = ''.join(temp)
                if word in hashmap:
                    hashmap[word]+=1
                else:
                    hashmap[word]=1
                temp=[]
            else:
                temp.append(s1[i])
        word = ''.join(temp)
        if word in hashmap:
            hashmap[word]+=1
        else:
            hashmap[word]=1
        temp=[]
        for i in range(len(s2)):
            if s2[i] == " ":
                word = ''.join(temp)
                if word in hashmap:
                    hashmap[word]+=1
                else:
                    hashmap[word]=1
                temp=[]
            else:
                temp.append(s2[i])
        word = ''.join(temp)
        if word in hashmap:
            hashmap[word]+=1
        else:
            hashmap[word]=1
        res=[]
        for key in hashmap:
            if hashmap[key]==1:
                res.append(key)
        return res