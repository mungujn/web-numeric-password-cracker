import unittest
from Sorter import Sorter
from PasswordTester import PasswordTester
from Filer import Filer

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.password_tester = PasswordTester()

    def test_recordTriedPassword(self):
        self.password_tester.recordTriedPassword(11111)
        items = Filer.readItemsFromFileToList("tried.txt")
        exists = items.index("11111")
        self.assertEquals(exists, 0)

    def test_sort(self):
        lst = [10, 3, 5, 7, 9]
        sorted_items = Sorter.selectionSort(lst)
        self.assertEqual(sorted_items[0], 3)


if __name__ == '__main__':
    unittest.main()
