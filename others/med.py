class MedianFinder:

    def __init__(self):
        self.list = list()
        

    def addNum(self, num: int) -> None:
        self.list.append(num)
        print(self.list)

    def findMedian(self) -> float:
        leng =len(self.list)
        if leng%2==1:
            return self.list[leng//2]
        else:
            print(leng//2)
            return (self.list[leng//2]+self.list[(leng//2)-1])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
a = MedianFinder()
a.addNum(1)
a.addNum(2)
print(a.findMedian())

