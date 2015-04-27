from System import *
from System.Collections.Generic import List
import clr

from random import shuffle

def main():
    list = [i for i in range(10)]
    shuffle(list)

    sorter = HeapSort()
    sortedList = sorter.sort(list)
    print sortedList

class HeapSort(object):
    def sort(self, list):
        self.buildHeap(list)
        end = len(list)

        while end > 1:
            list[0], list[end-1] = list[end-1], list[0]
            end -= 1

            self.siftDown(list, 0, end)
        return list 

    def buildHeap(self, list):
        start = (len(list) - 1) / 2

        while start >= 0:
            self.siftDown(list, start, len(list))
            start -= 1

    def siftDown(self, list, start, end):
        root = start
        leftChild = root * 2 + 1
        rightChild = leftChild + 1
        while leftChild < end:
            swap = root
            if list[swap] < list[leftChild]:
                swap = leftChild
            if rightChild < end and list[swap] < list[rightChild]:
                swap = rightChild

            if swap == root:
                return
            else:
                list[root], list[swap], root = list[swap], list[root], swap

            leftChild = root * 2 + 1
            rightChild = leftChild + 1

class SelectionSort(object):
    def sort(self, list):
        newList = []
        while len(list) > 0:
            max = -1
            maxIndex = -1
            for i in xrange(len(list)):
                if list[i] > max:
                    maxIndex = i
                    max = list[maxIndex]
            newList.insert(0, list.pop(maxIndex))
        return newList

if __name__ == "__main__":
    main()