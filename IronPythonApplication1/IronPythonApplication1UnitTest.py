import unittest
import random
from IronPythonApplication1 import *

class SortUnitTest(object):
    def setUp(self):
        '''Generates expected and actuals data. Actuals is a deep clone of expected data.
        '''
        self.expected = [i for i in range(100)]
        self.data = list(self.expected)

    def test_random(self):
        '''List is randomly shuffled.
        '''
        random.shuffle(self.data)
        self.assertNotEqual(self.data, self.expected, 'Two lists were not shuffled.')

        self.data = self.sorter.sort(self.data)
        self.compare()

    def test_reverse(self):
        '''List is reversed and sorted.
        '''
        self.data.reverse()
        self.data = self.sorter.sort(self.data)
        self.compare()

    def test_presorted(self):
        '''List is unchanged and sorted.
        '''
        self.data = self.sorter.sort(self.data)
        self.compare()

    def test_itemRemoved(self):
        '''One item is removed from list.
        '''
        self.data.pop()
        self.assertNotEqual(len(self.data), len(self.expected), 'Actual list has an element removed, it cannot be the same list as Expected.')

    def test_itemAdded(self):
        '''One item is added to list.
        '''
        self.data.append(len(self.data))
        self.assertNotEqual(len(self.data), len(self.expected), 'Actual list has an element removed, it cannot be the same list as Expected.')

    def compare(self):
        '''Set comparison between Expected and Actual should result a third list that is the same.
        '''
        equal = True
        if len(self.expected) != len(self.data):
            equal = False
        else:
            for i in xrange(len(self.expected)):
                if self.expected[i] != self.data[i]:
                    equal = False
                    break

        self.assertTrue(equal, 'The two lists are not identical.')

class HeapSortUnitTest(SortUnitTest, unittest.TestCase):
    def setUp(self):
        '''Sets up the heap sort tests.
        '''
        SortUnitTest.setUp(self)
        self.sorter = HeapSort()

    def test_buildHeap(self):
        list = range(10)
        self.sorter.buildHeap(list)
        self.assertEqual(list, [9,8,6,7,4,5,2,0,3,1], "Heap property was not satisfied on the heap.")

    def test_siftDown_oneItem(self):
        list = [0]
        self.sorter.siftDown(list, 0, len(list))
        self.assertEqual(list, [0], "The sift down algorithm is broken for trivial case.")

    def test_siftDown_twoItem_notSorted(self):
        list = [0,1]
        self.sorter.siftDown(list,0, len(list))
        self.assertEqual(list, [1,0], "The sift down algorithm is not doing comparison between parent and child correctly.")

    def test_siftDown_twoItem_alreadySorted(self):
        list = [1,0]
        self.sorter.siftDown(list,0, len(list))
        self.assertEqual(list, [1,0], "The sift down is sorting an already sorted heap.")

    def test_siftDown_fiveItem_alreadySorted(self):
        list = [4,2,3,0,1]
        self.sorter.siftDown(list,0, len(list))
        self.assertEqual(list, [4,2,3,0,1], "The sift down is sorting an already sorted heap.")

    def test_siftDown_fiveItem_notSorted(self):
        list = [4, 0, 1, 2, 3]
        self.sorter.siftDown(list,1, len(list))
        self.assertEqual(list, [4,3,1,2,0], "The sift down does not work for more than 1 level.")

class MergeSortUnitTest(SortUnitTest, unittest.TestCase):
    def setUp(self):
        SortUnitTest.setUp(self)
        self.sorter = MergeSort()

class BubbleSortUnitTest(SortUnitTest, unittest.TestCase):
    def setUp(self):
        SortUnitTest.setUp(self)
        self.sorter = BubbleSort()

class InsertionSortUnitTest(SortUnitTest, unittest.TestCase):
    def setUp(self):
        SortUnitTest.setUp(self)
        self.sorter = InsertionSort()

class SelectionSortUnitTest(SortUnitTest, unittest.TestCase):
    def setUp(self):
        SortUnitTest.setUp(self)
        self.sorter = SelectionSort()

def runAll():
    unittest.main()

def runSingleTest():
    tests = unittest.TestSuite()
    tests.addTest(InsertionSort('test_reverse'))
    unittest.TextTestRunner().run(tests)

def runSingleTestcase():
    tests = unittest.TestLoader().loadTestsFromTestCase(InsertionSortUnitTest)
    unittest.TextTestRunner().run(tests)

if __name__ == '__main__':
    runSingleTestcase()
