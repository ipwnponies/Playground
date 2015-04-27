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

class SelectionSortUnitTest(SortUnitTest, unittest.TestCase):
    def setUp(self):
        SortUnitTest.setUp(self)
        self.sorter = SelectionSort()

if __name__ == '__main__':
    unittest.main()