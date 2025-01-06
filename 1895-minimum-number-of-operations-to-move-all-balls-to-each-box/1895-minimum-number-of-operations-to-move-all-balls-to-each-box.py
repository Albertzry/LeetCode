class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = []
        for i in range(len(boxes)):
            s = sum(abs(j - i) for j, c in enumerate(boxes) if c == '1')
            res.append(s)
        return res
