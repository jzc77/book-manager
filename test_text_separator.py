"""
Unit test the text_separator function by identifying the disjointed equivalency partitions.
"""

from unittest import TestCase
from books import text_separator


class TestTextSeparator(TestCase):
    def test_text_separator_common_number(self):
        """Test a common number of dashes needed."""
        number_of_dashes = 77
        expected = "-----------------------------------------------------------------------------"
        actual = text_separator(number_of_dashes)
        self.assertEqual(expected, actual)

    def test_text_separator_one_dash(self):
        """Test one dash."""
        number_of_dashes = 1
        expected = "-"
        actual = text_separator(number_of_dashes)
        self.assertEqual(expected, actual)

    def test_text_separator_negative_dash(self):
        """Test a negative number of dashes."""
        number_of_dashes = -10
        expected = ""
        actual = text_separator(number_of_dashes)
        self.assertEqual(expected, actual)

    def test_text_separator_zero_dash(self):
        """Test zero dash."""
        number_of_dashes = 0
        expected = ""
        actual = text_separator(number_of_dashes)
        self.assertEqual(expected, actual)
