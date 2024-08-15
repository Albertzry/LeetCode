class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        ph = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r","s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        def com(char1, char2):
            reminder = []
            for i in range(len(char1)):
                for j in range(len(char2)):
                    reminder.append(char1[i] + char2[j])
            return reminder

        current = ph[digits[0]]
        for i in range(1,len(digits)):
            current = com(current, ph[digits[i]])
        return current
