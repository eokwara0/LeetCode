import unittest
import src.length_of_last_word.length_of_last_word as lolw


class TestLOLW(unittest.TestCase):

    def test_helloWorld(self):
        self.assertEqual(
            lolw.Solution().lengthOfLastWord("Hello World"), 5
        )
    
    def test_two(self):
        self.assertEqual(
            lolw.Solution().lengthOfLastWord("   fly me to     the moon  ") , 4
                         )
    def test_three(self):
        self.assertEqual(lolw.Solution().lengthOfLastWord("luffy is still joyboy"),6)


if __name__ == '__main__':
    unittest.main()