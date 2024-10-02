class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        hashmap = dict()
        temp = arr[:]
        temp = sorted(set(temp))
        for i,num in enumerate(temp):
            hashmap[num] = i+1
        ans = []
        for num in arr:
            ans.append(hashmap[num])
        return ans

