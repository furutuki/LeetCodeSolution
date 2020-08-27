import heapq


class MaxHeapObj(object):
    def __init__(self, val): self.val = val

    def __lt__(self, other): return self.val > other.val

    def __eq__(self, other): return self.val == other.val

    def __str__(self): return str(self.val)


class MinHeap(object):
    def __init__(self): self.h = []

    def heappush(self, x): heapq.heappush(self.h, x)

    def heappop(self): return heapq.heappop(self.h)

    def __getitem__(self, i): return self.h[i]

    def __len__(self): return len(self.h)


class MaxHeap(MinHeap):
    def heappush(self, x): heapq.heappush(self.h, MaxHeapObj(x))

    def heappop(self): return heapq.heappop(self.h).val

    def __getitem__(self, i): return self.h[i].val


class MedianFinder:

    def __init__(self):
        self.minHeap = MinHeap()
        self.maxHeap = MaxHeap()

    def addNum(self, num: int) -> None:
        self.maxHeap.heappush(num)
        n = self.maxHeap.heappop()
        self.minHeap.heappush(n)
        sizeDiff = len(self.minHeap) - len(self.maxHeap)
        if sizeDiff > 1 or sizeDiff < 0:
            self.maxHeap.heappush(self.minHeap.heappop())

    def findMedian(self) -> float:
        m, n = len(self.maxHeap), len(self.minHeap)
        if m == n:
            return (self.maxHeap.__getitem__(0) + self.minHeap.__getitem__(0)) / 2
        else:
            return self.minHeap.__getitem__(0)
