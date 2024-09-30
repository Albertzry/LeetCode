class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.stack=[]
        self.n=maxSize

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack)<self.n:
            self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack.pop()
        else:
            return -1

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        for i in range(min(len(self.stack),k)):
            self.stack[i]+=val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)