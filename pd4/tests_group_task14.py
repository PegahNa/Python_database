import unittest

from .group_task14 import min_waiting_time


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        patients = [3, 2, 1, 2, 6]
        expected = 17
        actual = min_waiting_time(patients)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        patients = [2, 1, 1, 1]
        expected = 6
        actual = min_waiting_time(patients)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        patients = [1, 2, 4, 5, 2, 1]
        expected = 23
        actual = min_waiting_time(patients)
        self.assertEqual(actual, expected)

    def test_case_4(self):
        patients = [25, 30, 2, 1]
        expected = 32
        actual = min_waiting_time(patients)
        self.assertEqual(actual, expected)

    def test_case_5(self):
        patients = [1, 1, 1, 1, 1]
        expected = 10
        actual = min_waiting_time(patients)
        self.assertEqual(actual, expected)

    def test_case_6(self):
        patients = [4, 3, 1, 1, 3, 2, 1, 8]
        expected = 45
        actual = min_waiting_time(patients)
        self.assertEqual(actual, expected)

    def test_case_7(self):
        patients = [2]
        expected = 0
        actual = min_waiting_time(patients)
        self.assertEqual(actual, expected)

    def test_case_8(self):
        patients = [5, 4, 3, 2, 1]
        expected = 20
        actual = min_waiting_time(patients)
        self.assertEqual(actual, expected)

    def test_case_9(self):
        patients = [1, 2, 3, 4, 5]
        expected = 20
        actual = min_waiting_time(patients)
        self.assertEqual(actual, expected)

    def test_case_10(self):
        patients = [1, 1, 1, 4, 5, 6, 8, 1, 1, 2, 1]
        expected = 81
        actual = min_waiting_time(patients)
        self.assertEqual(actual, expected)

    def test_case_error(self):
        patients = "invalid input"
        with self.assertRaises(TypeError):
            min_waiting_time(patients)


