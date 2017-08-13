from unittest import TestCase

import numpy as np
from my_answers import *

class TestMyAnswer(TestCase):
    def test_window_transform_series(self):
        odd_nums = np.array([1, 3, 5, 7, 9, 11, 13])
        window_size = 2

        expected_X = []
        expected_X.append(odd_nums[0:2])
        expected_X.append(odd_nums[1:3])
        expected_X.append(odd_nums[2:4])
        expected_X.append(odd_nums[3:5])
        expected_X.append(odd_nums[4:6])


        expected_y = odd_nums[2:]

        expected_X = np.asarray(expected_X)
        expected_y = np.asarray(expected_y)
        expected_y = np.reshape(expected_y, (len(expected_y), 1))  # optional

        # assert (type(expected_X).__name__ == 'ndarray')
        # assert (type(expected_y).__name__ == 'ndarray')
        # assert (expected_X.shape == (5, 2))
        # assert (expected_y.shape in [(5, 1), (5,)])

        actual_X, actual_y = window_transform_series(odd_nums, window_size)

        np.testing.assert_array_equal(actual_X, expected_X)
        np.testing.assert_array_equal(actual_y, expected_y)

    def test_window_transform_text(self):
        # first 10 alphabet
        text = "abcdefghij"

        assert len(text) == 10

        window_size = 4
        step_size = 2

        expected_input = [
            "abcd",
            "cdef",
            "efgh"
        ]

        expected_output = [
            'e',
            'g',
            'i'
        ]

        actual_input, actual_output = window_transform_text(
            text, window_size, step_size)

        self.assertListEqual(actual_input, expected_input)
        self.assertListEqual(actual_output, expected_output)

        window_size = 3
        step_size = 2

        expected_input = [
            "abc",
            "cde",
            "efg",
            "ghi",
        ]

        expected_output = [
            'd',
            'f',
            'h',
            'j'
        ]

        actual_input, actual_output = window_transform_text(
            text, window_size, step_size)

        self.assertListEqual(actual_input, expected_input)
        self.assertListEqual(actual_output, expected_output)

