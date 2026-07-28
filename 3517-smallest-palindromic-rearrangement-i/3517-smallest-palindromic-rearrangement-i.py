class Solution:
    def smallestPalindrome(self, s: str) -> str:
        sl = list(s)
        n = len(sl)
        front = sl[:int(floor(n/2))]
        front.sort()
        mid = [sl[int(floor(n/2))]] if n%2 else []
        back = front[::-1]
        return "".join(front+mid+back)