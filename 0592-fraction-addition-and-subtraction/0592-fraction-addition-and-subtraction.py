class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        x, y = 0, 1 
        i, n = 0, len(expression)
        while i < n:
            x1, sign = 0, 1
            if expression[i] == '-' or expression[i] == '+':
                if expression[i] == '-':
                    sign = -1
                i += 1
            while i < n and expression[i].isdigit():
                x1 = x1 * 10 + int(expression[i])
                i += 1
            x1 = sign * x1
            i += 1

            y1 = 0
            while i < n and expression[i].isdigit():
                y1 = y1 * 10 + int(expression[i])
                i += 1

            x = x * y1 + x1 * y
            y *= y1
        if x == 0:
            return "0/1"

        common_divisor = 1
        for i in range(1, min(y, abs(x))+1):
            if y % i == 0 and x % i == 0:
                common_divisor = i

        return str(x // common_divisor) + "/" + str(y // common_divisor)


