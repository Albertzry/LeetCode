class Solution(object):
    def findWinningPlayer(self, skills, k):
        """
        :type skills: List[int]
        :type k: int
        :rtype: int
        """
        max_i = win = 0
        for i in range(1, len(skills)):
            if skills[i] > skills[max_i]:
                max_i = i
                win = 0
            win += 1 
            if win == k: 
                break
        return max_i
