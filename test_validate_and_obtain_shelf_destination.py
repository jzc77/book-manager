"""
Unit test the validate_and_obtain_shelf_destination function by identifying the disjointed equivalency partitions.
"""

from unittest import TestCase
from unittest.mock import patch
import books


class TestValidateAndObtainShelfDestination(TestCase):
    @patch('builtins.input', side_effect=["3"])
    def test_validate_and_obtain_integer_shelf_destination(self, mock_input):
        """Test expected user input for searching a shelf that is an integer."""
        actual = books.validate_and_obtain_shelf_destination()
        expected = "3"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["43"])
    def test_validate_and_obtain_named_shelf_destination(self, mock_input):
        """Test expected user input for searching a shelf that has a name."""
        actual = books.validate_and_obtain_shelf_destination()
        expected = "Reading"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["ffeytfr3q2r3wgq3r", "4"])
    def test_invalid_shelf_entered(self, mock_input):
        """Test no user input."""
        actual = books.validate_and_obtain_shelf_destination()
        expected = "4"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["0", "4"])
    def test_shelf_zero(self, mock_input):
        """Test no user input."""
        actual = books.validate_and_obtain_shelf_destination()
        expected = "4"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["", "4"])
    def test_no_shelf_entered(self, mock_input):
        """Test no user input."""
        actual = books.validate_and_obtain_shelf_destination()
        expected = "4"
        self.assertEqual(expected, actual)
