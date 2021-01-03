"""
Unit test the search_term function by identifying the disjointed equivalency partitions.
"""

from unittest import TestCase
from unittest.mock import patch
import books


class TestSearchTerm(TestCase):
    @patch('builtins.input', side_effect=["Architecture"])
    def test_common_search_term(self, mock_input):
        """Test common user input for searching a book."""
        actual = books.search_term()
        expected = "Architecture"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[""])
    def test_no_search_term(self, mock_input):
        """Test no search term entered."""
        actual = books.search_term()
        expected = ""
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["32"])
    def test_integer_search_term(self, mock_input):
        """Test integer search term."""
        actual = books.search_term()
        expected = "32"
        self.assertEqual(expected, actual)