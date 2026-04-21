class MedianFinder:

    def __init__(self):
        self.arr = []
        self.size = 0

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.size += 1
        self.arr.sort()

    def findMedian(self) -> float:
        if self.size % 2 == 0:
            return (self.arr[self.size // 2] + self.arr[(self.size // 2) - 1]) / 2
        else:
            return self.arr[self.size // 2]
        