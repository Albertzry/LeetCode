class Trie(object):
    def __init__(self):
        self.child=dict()
        self.isEnd=False

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self
        for c in word:
            if c not in cur.child:
                cur.child[c] = Trie()
            cur = cur.child[c]
        cur.isEnd = True
        
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cur = self
        for c in word:
            if c in cur.child:
                cur = cur.child[c]
            else:
                return False
        return cur.isEnd
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        cur = self
        for c in prefix:
            if c in cur.child:
                cur = cur.child[c]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)