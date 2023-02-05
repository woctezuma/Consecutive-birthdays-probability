import unittest

import get_confidence_interval
import get_solution


class TestGetConfidenceIntervalMethods(unittest.TestCase):
    def test_main(self):
        self.assertTrue(get_confidence_interval.main())


class TestGetSolutionMethods(unittest.TestCase):
    def test_main(self):
        self.assertTrue(get_solution.main())


if __name__ == "__main__":
    unittest.main()
