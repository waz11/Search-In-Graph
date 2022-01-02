import sys

class Element:
    def __init__(self, rank, element=''):
        self.rank = rank
        self.element = element

class MaxHeap:
    def __init__(self, maxsize=20):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [Element(0)] * (self.maxsize + 1)
        self.Heap[0] = Element(sys.maxsize)
        self.FRONT = 1

    def parent(self, pos):
        return pos // 2

    def leftChild(self, pos):
        return 2 * pos

    def rightChild(self, pos):
        return (2 * pos) + 1

    def isLeaf(self, pos):
        if pos >= (self.size // 2) and pos <= self.size:
            return True
        return False

    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = (self.Heap[spos],
                                            self.Heap[fpos])

    def maxHeapify(self, pos):
        if not self.isLeaf(pos):
            if (self.Heap[pos].rank < self.Heap[self.leftChild(pos)].rank or
                    self.Heap[pos].rank < self.Heap[self.rightChild(pos)].rank):
                if (self.Heap[self.leftChild(pos)].rank >
                        self.Heap[self.rightChild(pos)].rank):
                    self.swap(pos, self.leftChild(pos))
                    self.maxHeapify(self.leftChild(pos))
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.maxHeapify(self.rightChild(pos))


    def insert(self, rank, component):
        element = Element(rank, component)
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element
        current = self.size
        while (self.Heap[current].rank > self.Heap[self.parent(current)].rank):
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def Print(self):
        for i in range(1, (self.size // 2) + 1):
            print(" PARENT : " + str(self.Heap[i]) +
                  " LEFT CHILD : " + str(self.Heap[2 * i]) +
                  " RIGHT CHILD : " + str(self.Heap[2 * i + 1]))

    def extractMax(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.maxHeapify(self.FRONT)
        return popped


if __name__ == "__main__":
    maxHeap = MaxHeap(15)
    e1 = Element(3)
    e2 = Element(2)
    e3 = Element(5)
    maxHeap.insert(e1)
    maxHeap.insert(e3)
    maxHeap.insert(e2)

    maxHeap.Print()
    print("The Max val is " + str(maxHeap.extractMax().rank))
