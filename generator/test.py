import unittest
from main import LeetCodeSource

class TestLeetCodeSource(unittest.TestCase):

    def test_get_md_solution_link(self):
        test1 = LeetCodeSource("Reverse Integer", "https://leetcode.com/problems/reverse-integer/", "iwntslp")
        expect = "+[Reverse Integer](#reverse-integer)"

        result = test1.get_md_solution_link()

        self.assertEqual(expect, result)



    if __name__ == '__main__':
        unittest.main()
