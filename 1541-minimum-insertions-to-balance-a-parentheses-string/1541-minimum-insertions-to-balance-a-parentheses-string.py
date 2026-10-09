class Solution:
    def minInsertions(self, s: str) -> int:
        length = len(s)
        insertions = leftCount = index = 0

        while index < length:
            if s[index] == "(":
                leftCount += 1
                index += 1
            else:
                if leftCount > 0:
                    leftCount -= 1
                else:
                    insertions += 1
                if index < length - 1 and s[index + 1] == ")":
                    index += 2
                else:
                    insertions += 1
                    index += 1
        
        insertions += leftCount * 2
        return insertions
