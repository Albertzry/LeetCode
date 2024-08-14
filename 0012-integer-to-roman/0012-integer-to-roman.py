class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ""
        ex = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        num_str = str(num)
        n = m = len(num_str)
        reminder = num
        for i in range(m):
            temp = reminder // 10 ** (n - 1)
            reminder = reminder % 10 **(n - 1)
            if temp != 4 and temp != 9:
                if temp >= 5:
                    result += ex[5 * (10 ** (n - 1))]
                    for j in range(temp - 5):
                        result += ex[10 ** (n - 1)]
                else:
                    for j in range(temp):
                        result += ex[10 ** (n - 1)]
            elif temp == 4:
                result += ex[10 ** (n - 1)]
                result += ex[5 * (10 ** (n - 1))]
            else:
                result += ex[10 ** (n-1)]
                result += ex[10 ** (n)]
            n -= 1
        return result 