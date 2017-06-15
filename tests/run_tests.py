"""
Test Suite for Pi Romulus.
"""
import unittest

TESTS = []

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suites_list = []
    for test_class in TESTS:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)
