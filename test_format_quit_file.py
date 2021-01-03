"""
Unit test the format_quit_file function by identifying the disjointed equivalency partitions.
"""

from unittest import TestCase
from books import format_quit_file


class TestFormatQuitFile(TestCase):
    def test_format_two_quit_file_lines(self):
        """Test multi-line formatting to replace file."""
        book_values = ["Dupre", "Skyscrapers", "BD&L", "Gaby", "Architecture", "20th Century", "Hollingsworth",
                       "Architecture of the 20th Century", "Exeter", "6", "Architecture", "20th Century"]
        expected = 'Dupre	Skyscrapers	BD&L	Gaby	Architecture	20th Century	Hollingsworth	Architecture' \
                   ' of the 20th Century	Exeter	6	Architecture	20th Century'
        actual = format_quit_file(book_values)
        self.assertEqual(expected, actual)

    def test_format_partial_file_lines(self):
        """Test one line formatting to replace file."""
        book_values = ["Author", "Dupre"]
        expected = 'Author	Dupre'
        actual = format_quit_file(book_values)
        self.assertEqual(expected, actual)

    def test_format_empty_file_lines(self):
        """Test empty line formatting to replace file."""
        book_values = []
        expected = ''
        actual = format_quit_file(book_values)
        self.assertEqual(expected, actual)
