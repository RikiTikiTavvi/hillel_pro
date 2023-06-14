import unittest

from unittest.mock import patch
from lesson2.drunk_polish_calculator import main, op_plus, op_minus, op_multiply, op_divide


class TestCalculator(unittest.TestCase):
    def test_op_plus(self):
        input_cases = [(1, 1, 2),
                       (2, 3, 5),
                       (567, 342, 909)
                       ]
        for x, y, extended in input_cases:
            result = op_plus(x, y)
            self.assertEqual(result, extended)

    def test_op_minus(self):
        input_cases = [(1, 1, 0),
                       (2, 3, -1),
                       (567, 342, 225)
                       ]
        for x, y, extended in input_cases:
            result = op_minus(x, y)
            self.assertEqual(result, extended)

    def test_op_multiply(self):
        input_cases = [(1, 1, 1),
                       (2, 3, 6),
                       (567, 342, 193914)
                       ]
        for x, y, extended in input_cases:
            result = op_multiply(x, y)
            self.assertEqual(result, extended)

    def test_op_divide(self):
        input_cases = [(1, 1, 1),
                       (2, 2, 1),
                       (566, 2, 283)
                       ]
        for x, y, extended in input_cases:
            result = op_divide(x, y)
            self.assertEqual(result, extended)


class TestMain(unittest.TestCase):

    def test_main(self):
        input_string = "1 2 + 3 * 4 -"
        expected_output = 5

        with patch("builtins.input", return_value=input_string):
            with patch("builtins.print") as mock_print:
                main()

                mock_print.assert_called_with(expected_output)


if __name__ == '__main__':
    unittest.main()
