import unittest

import get_confidence_interval
import get_solution


class TestGetConfidenceIntervalMethods(unittest.TestCase):
    def test_main(self):
        assert get_confidence_interval.main() is True


class TestGetSolutionMethods(unittest.TestCase):
    def test_main(self):
        assert get_solution.main() is True


if __name__ == "__main__":
    unittest.main()
