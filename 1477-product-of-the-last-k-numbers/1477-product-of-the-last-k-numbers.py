class ProductOfNumbers:
    def __init__(self):
        self.p = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.p = [1]
        else:
            self.p.append(self.p[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.p): return 0
        return self.p[-1] // self.p[-k-1]



# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)