import unittest
from main import twoSum
class TestTwoSum(unittest.TestCase):
    def test_two_sum_simple_case(self):
        self.assertEqual(twoSum([2,7,11,15],9), [0,1])
    def test_two_sum_simple_case1(self):
        self.assertEqual(twoSum([3,2,4], 6), [1,2])
    def test_two_sum_simple_case2(self):
        self.assertEqual(twoSum([3,3], 6), [0,1])
    def test_two_sum_simple_case3(self):
        self.assertEqual(twoSum([3.9872087342,322.34], 6), None)
    def test_two_sum_simple_case4(self):
        self.assertEqual(twoSum([], 6), None)
    def test_two_sum_simple_case5(self):
        self.assertEqual(twoSum(['2342',3,'3432'], 6), None)
    def test_two_sum_simple_case6(self):
        self.assertEqual(twoSum([32,3,56,3], 6), [1,3])
    def test_two_sum_simple_case7(self):
        self.assertEqual(twoSum([32,56,39], 6), None)
    def test_two_sum_simple_case8(self):
        self.assertEqual(twoSum([1,0,2,3,], 6), None)

if __name__=='__main__':
    unittest.main()