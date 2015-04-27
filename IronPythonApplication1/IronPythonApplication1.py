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