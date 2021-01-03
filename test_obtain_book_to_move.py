"""
Unit test the obtain_book_to_move function by identifying the disjointed equivalency partitions.
"""

from unittest import TestCase
from unittest.mock import patch
import books


class TestObtainBookToMove(TestCase):
    @patch('builtins.input', side_effect=["3"])
    def test_obtain_book_to_move_with_integer_input(self, mock_input):
        """Test expected user input to select a book result."""
        actual = books.validate_and_obtain_shelf_destination()
        expected = "3"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["Book 1", "5"])
    def test_invalid_book_to_move_input(self, mock_input):
        """Test invalid alphanumeric user input for searching a book result."""
        actual = books.validate_and_obtain_shelf_destination()
        expected = "5"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["1000", "5"])
    def test_out_of_range_input(self, mock_input):
        """Test out of range user input for searching a book result."""
        actual = books.validate_and_obtain_shelf_destination()
        expected = "5"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["0", "5"])
    def test_invalid_zero_input(self, mock_input):
        """Test user input of zero for searching a book result."""
        actual = books.validate_and_obtain_shelf_destination()
        expected = "5"
        self.assertEqual(expected, actual)
