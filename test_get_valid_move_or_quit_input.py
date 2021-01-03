"""
Unit test the get_valid_move_or_quit_input function by identifying the disjointed equivalency partitions.
"""

from unittest import TestCase
from unittest.mock import patch
import books


class TestGetValidMoveOrQuitInput(TestCase):
    @patch('builtins.input', side_effect=["1"])
    def test_get_valid_move_input(self, mock_input):
        """Test expected user input for moving book."""
        actual = books.get_valid_move_or_quit_input()
        expected = "1"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["2"])
    def test_quit_input(self, mock_input):
        """Test expected user input to quit program."""
        actual = books.get_valid_move_or_quit_input()
        expected = "quit"
        self.assertEqual(expected, actual)

