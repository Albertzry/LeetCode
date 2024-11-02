class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        sentence=sentence.split(" ")
        if not sentence[0][0]==sentence[-1][-1]:
            return False
        for i in range(1,len(sentence)):
            if sentence[i][0]!=sentence[i-1][-1]:
                return False
        return True