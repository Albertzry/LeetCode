class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.que=[]
        self.maxSize=k

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.que)==self.maxSize:
            return False
        self.que=[value]+self.que
        return True
        
    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.que)==self.maxSize:
            return False
        self.que.append(value)
        return True

    def deleteFront(self):
        """
        :rtype: bool
        """
        if not self.que:
            return False
        self.que.pop(0)
        return True

    def deleteLast(self):
        """
        :rtype: bool
        """
        if not self.que:
            return False
        self.que.pop(-1)
        return True

    def getFront(self):
        """
        :rtype: int
        """
        if not self.que:
            return -1
        return self.que[0]

    def getRear(self):
        """
        :rtype: int
        """
        if not self.que:
            return -1
        return self.que[-1]

    def isEmpty(self):
        """
        :rtype: bool
        """
        if not self.que:
            return True
        return False

    def isFull(self):
        """
        :rtype: bool
        """
        if len(self.que)==self.maxSize:
            return True
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()