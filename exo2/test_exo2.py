def solution(string, ending):
    return string.endswith(ending)
import unittest

class TestSolution(unittest.TestCase):

    def test_fixed_tests_true(self):
        fixed_tests_True = (
            ("samurai", "ai"),
            ("ninja",   "ja"),
            ("sensei",  "i"),
            ("abc",     "abc"),
            ("abcabc",  "bc"),
            ("fails",   "ails"),
        )
        for string, ending in fixed_tests_True:
            with self.subTest(f"{string} should end with {ending}"):
                self.assertTrue(solution(string, ending))

    def test_fixed_tests_false(self):
        fixed_tests_False = (
            ("sumo",    "omo"),
            ("samurai", "ra"),
            ("abc",     "abcd"),
            ("ails",    "fails"),
            ("this",    "fails"),
            ("spam",    "eggs"),
        )
        for string, ending in fixed_tests_False:
            with self.subTest(f"{string} should not end with {ending}"):
                self.assertFalse(solution(string, ending))

# If you want to run the tests directly, you can do so using:
if __name__ == '__main__':
    unittest.main()