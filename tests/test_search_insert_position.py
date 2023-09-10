import unittest
import src.search_insert_position.search_insert_position as sip

class TestSIP(unittest.TestCase):
    def test_initial(self):
        self.assertEqual(
            sip.Solution().searchInsert([1] , 0),0
        )
    def test_last_value(self):
        self.assertEqual(
            sip.Solution().searchInsert([1,3,5,6] , 7),4
        )
if __name__ == '__main__':
    unittest.main()