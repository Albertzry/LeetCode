class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill = sorted(skill)
        l,r,ans = 0 , len(skill)-1 , 0
        temp = skill[l]+skill[r]
        while l<r:
            if skill[l]+skill[r] != temp:
                return -1
            ans += skill[l]*skill[r]
            l+=1
            r-=1
        return ans
