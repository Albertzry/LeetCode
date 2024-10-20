class Solution(object):
    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """
        stack = []
        expression = list(expression)
        while expression:
            c = expression.pop(0)
            if c == ')':
                temp_exp = []
                while stack[-1] != '(':
                    conv = stack.pop(-1)
                    if conv == ',':
                        continue
                    elif conv == 't':
                        temp_exp.append(True)
                    elif conv == 'f':
                        temp_exp.append(False)
                stack.pop(-1)
                if stack[-1] == '!':
                    temp = not temp_exp[0]
                elif stack[-1] == '&':
                    temp = False if False in temp_exp else True
                elif stack[-1] == '|':
                    temp = True if True in temp_exp else False
                stack.pop(-1)
                if temp == True:
                    stack.append('t')
                elif temp == False:
                    stack.append('f')
            else:
                stack.append(c)
        if stack[0] == 't':
            return True
        else:
            return False   