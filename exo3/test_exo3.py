import unittest

from exo3 import processLines


class TestExo3(unittest.TestCase):
    def test_input_1(self):
        with open("sample/input1.txt") as input1:
            lines = input1.readlines()

        with open("sample/output1.txt") as output1:
            expected = output1.read()

        self.assertEqual(expected, processLines(lines))

    # Ecrire une autre méthode pour vérifier le second use case

