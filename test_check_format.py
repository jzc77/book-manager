"""
Unit test the check_format function by identifying the disjointed equivalency partitions.
"""

from unittest import TestCase
from books import check_format


class TestCheckFormat(TestCase):
    def test_check_format_one_line(self):
        """Test one line formatting from file."""
        line_from_file = "Dupre	Skyscrapers	BD&L	12	Architecture	20th Century"
        expected = ['Dupre', 'Skyscrapers', 'BD&L', '12', 'Architecture', '20th Century']
        actual = check_format(line_from_file)
        self.assertEqual(expected, actual)

    def test_check_format_two_lines(self):
        """Test two line formatting from file."""
        line_from_file = "Dupre	Skyscrapers	BD&L	12	Architecture	20th Century \
        Hollingsworth	Architecture of the 20th Century	Exeter	6	Architecture	20th Century"
        expected = ['Dupre', 'Skyscrapers', 'BD&L', '12', 'Architecture', '20th Century         Hollingsworth',
                    'Architecture of the 20th Century', 'Exeter', '6', 'Architecture', '20th Century']
        actual = check_format(line_from_file)
        self.assertEqual(expected, actual)

    def test_check_format_no_lines(self):
        """Test no line formatting from file."""
        line_from_file = ""
        expected = ['']
        actual = check_format(line_from_file)
        self.assertEqual(expected, actual)
