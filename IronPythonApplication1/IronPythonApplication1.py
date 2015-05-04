from System import *
from System.Collections.Generic import List
import clr

import random

def main():
    list = [i for i in range(10)]
    random.shuffle(list)

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

class MergeSort(object):
    def sort(self, list):
        return self.topDownSort(list)

    def bottomUpSort(self, list):
        '''Sort with bottom up approach. Each element is sorted within itself. Then merge with its neighbours.
        '''
        width = 1
        while width < len(list):
            i = 0
            while i < len(list):
                list[i:i+2*width] = self.merge(list[i:i + width], list[i + width: i + 2*width])
                i += 2 * width 
            width *= 2
        return list

    def topDownSort(self, list):
        '''Sort with top down approach. This is the common approach when thinking of merge sort.
        '''
        if len(list) <= 1:
            return list
        splitcount = len(list) / 2
        return self.merge(self.sort(list[:splitcount]), self.sort(list[splitcount:]))

    def merge(self, lista, listb):
        '''Merge the two lists, ordering the elements from both list.
        '''
        sortedList = []
        while len(lista) > 0 and len(listb) > 0:
            if lista[0] < listb[0]:
                sortedList.append(lista.pop(0))
            else:
                sortedList.append(listb.pop(0))

        # Add remaining items in list. Either lista or listb is empty at this time.
        sortedList.extend(lista)
        sortedList.extend(listb)
        return sortedList

class QuickSort(object):
    '''
    Quicksort is an exchange sorting algorithm. It works by selecting an element as the pivot, then partitioning
    items into a list of smaller elements and a list of larger elements. The partitions are recursively quicksorted.
    After the lists are sorted, the two lists and pivot are combined (in order) and result in a the whole sorted list.
    '''

    def sort(self, list):
        if len(list) <= 1:
            # Trivial case, sorted by definition.
            return list
        else:
            # Randomly select pivot.
            pivot = random.randint(0, len(list) - 1)
            count = len(list) - 1

            # Temporarily store the pivot value at the end of the list.
            list[pivot], list[count] = list[count], list[pivot]

            # Initialize the final pivot index.
            pivot = 0

            for i in xrange(len(list)):
                # For each item in the list, if it is less than the pivot value, insert it before the pivot index.
                if list[i] < list[count]:
                    list[i], list[pivot] = list[pivot], list[i]
                    pivot += 1

            # Swap the pivot back to its final location.
            list[pivot], list[count] = list [count], list[pivot]

            # Sort the partitions recursively.
            firstPartition = self.sort(list[:pivot])
            secondPartition = self.sort(list[pivot:])

            firstPartition.extend(secondPartition)
            return firstPartition

class BubbleSort(object):
    def sort(self, list):
        for i in xrange(len(list) - 1):
            for j in xrange(len(list) - 1 - i):
                if list[j] > list[j + 1]:
                    list[j], list[j+1] = list[j+1], list[j]
        return list

class InsertionSort(object):
    def sort(self, list):
        for i in xrange(len(list)):
            maxIndex = i
            for j in xrange(i, len(list)):
                if list[j] < list[maxIndex]:
                    maxIndex = j
            list[maxIndex], list[i] =  list[i], list[maxIndex]
        return list

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
