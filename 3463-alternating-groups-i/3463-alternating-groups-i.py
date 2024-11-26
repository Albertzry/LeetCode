class Solution(object):
    def numberOfAlternatingGroups(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        newColors = colors + colors[:2]
        count = 0

        for i in range(len(newColors)-2):
            if newColors[i] == 0:
                if newColors[i+1] == 1 and newColors[i+2] == 0:
                    count += 1
            if newColors[i] == 1:
                if newColors[i+1] == 0 and newColors[i+2] == 1:
                    count += 1
        return count