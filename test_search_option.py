"""
Unit test the search_option function by identifying the disjointed equivalency partitions.
"""

from unittest import TestCase
from unittest.mock import patch
import books


class TestSearchOption(TestCase):
    @patch('builtins.input', side_effect=["2"])
    def test_search_option_header(self, mock_input):
        """Test expected user input for searching a header."""
        actual = books.search_option()
        expected = "Title"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["7"])
    def test_search_option_quit(self, mock_input):
        """Test expected user input for quitting."""
        actual = books.search_option()
        expected = "quit"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["53", "7"])
    def test_invalid_search_option(self, mock_input):
        """Test invalid user input for searching a header."""
        actual = books.search_option()
        expected = "quit"
        self.assertEqual(expected, actual)
