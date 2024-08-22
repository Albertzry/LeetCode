class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1=="0"or num2=="0":
            return "0"
        result = 0
        for i in range(len(num1)):
            for j in range(len(num2)):
                result+=(int(num1[i])*int(num2[j]))*10**(len(num1)-i+len(num2)-j-2)
        return str(result)