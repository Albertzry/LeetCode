class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map = dict()
        for ch in strs:
            temp = ''.join(sorted(ch))
            if temp not in map:
                map[temp] = [ch]
            else:
                map[temp].append(ch)
        result = []
        for key in map:
            result.append(map[key])
        return result