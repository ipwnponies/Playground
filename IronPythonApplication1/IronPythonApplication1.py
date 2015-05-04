from System import *
from System.Collections.Generic import List
import clr
import sys

from random import shuffle

def main():
    list = [i for i in range(10)]
    shuffle(list)

    sorter = HeapSort()
    sortedList = sorter.sort(list)
    print sortedList

class HeapSort(object):
    '''
    Heapsort is a selection based sort. A heap is generated and the root is iteratively removed to the sorted array output.
    The heap is continually rebuilt after each removal to reform smaller heaps.
    Because a heap is created and items are moved around, this sort is not stable. It sorts in-place.
    '''

    def sort(self, list):
        self.buildHeap(list)
        end = len(list)

        while end > 1:
            list[0], list[end-1] = list[end-1], list[0]
            end -= 1

            self.siftDown(list, 0, end)
        return list 

    def buildHeap(self, list):
        '''Builds a heap by adding elements to the root and then applying siftDown.
        ''' 
        # Start building heap with the first non-leaf nodes.
        start = (len(list) - 1) / 2

        # Move up the heap, continually enforcing the heap property.
        while start >= 0:
            self.siftDown(list, start, len(list))
            start -= 1

    def siftDown(self, list, start, end):
        '''Apply heap property to tree.
        '''
        root = start
        leftChild = root * 2 + 1
        rightChild = leftChild + 1

        # Find the largest node. If it is one of the children, swap the nodes and then recurse into
        # that branch to ensure the heap property. If no swap is needed, no heap property has been changed, so we can return (minor optimization).
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
    '''
    Merge sort is a comparison sort. It is stable and is done in-place. A common optimization is to start with bottom up approach,
    replacing the recursion aspect with an iteration.
    '''
    def sort(self, list):
        return self.topDownSort(list)

    def bottomUpSort(self, list):
        '''Sort with bottom up approach. Each element is sorted within itself. Then merge with its neighbours.
        '''

        # width is the amonunt of elements in a list. Starting with the trivially sorted 1 element list, we increase this until the width is the entire list.
        width = 1
        while width < len(list):
            i = 0

            # Merge adjacent lists together.
            while i < len(list):
                list[i:i+2*width] = self.merge(list[i:i + width], list[i + width: i + 2*width])
                i += 2 * width 

            # Move up to the next level as all adjacent lists have now been merged into larger lists.
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

class BubbleSort(object):
    '''
    Bubble sort is a comparison sort. Each pass moves elements until the largest element is pushed to the end.
    A consequence of this is an optimization to check only n-i elements after each pass.
    '''
    def sort(self, list):
        for i in xrange(len(list) - 1):
            # Only need to check the remaining items, the previous i elements have be sorted to the end.
            for j in xrange(len(list) - 1 - i):
                if list[j] > list[j + 1]:
                    list[j], list[j+1] = list[j+1], list[j]
        return list

class InsertionSort(object):
    '''
    Insertion sort is a insertion sort. Each element is inserted to the sorted list in the right location.
    An optimization is to only check the remaining unsorted list.
    '''
    def sort(self, list):
        # First element is considered trivially sorted with itself.
        sortedIndex = 0

        # For each element in unsorted list, insert it into sorted order in sorted array.
        for i in xrange(sortedIndex, len(list)):
            # Find where element should be inserted in sorted array.
            for k in xrange(0, sortedIndex):
                if list[i] < list[k]:
                    list.insert(k, list.pop(i))
                    break
            sortedIndex += 1

        return list

class SelectionSort(object):
    '''
    Selection sort is selection sort. The smallest element is found from list and appended to the sorted list.
    The next smallest is found and appended, and so on.
    '''
    def sort(self, list):
        for i in xrange(len(list)):
            maxIndex = i

            # Find smallest element in remaining range.
            for j in xrange(i, len(list)):
                if list[j] < list[maxIndex]:
                    maxIndex = j

            # Move the smallest element to the sorted list.
            list[maxIndex], list[i] =  list[i], list[maxIndex]
        return list

if __name__ == "__main__":
    main()
