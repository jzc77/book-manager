"""
Unit test the search_books function by identifying the disjointed equivalency partitions.
"""

from unittest import TestCase
from books import search_books


class TestSearchBooks(TestCase):
    def test_valid_search_books(self):
        """Test common inputs."""
        user_search_option = "Author"
        user_search_term = "tre"
        expected = ['Author', 'Longstreth', 'Title', 'On the Edge of the World Four Architects in SF at the Turn of the'
                    ' Century', 'Publisher', 'University of California Press', 'Shelf', '5', 'Category', 'Architecture',
                    'Subject', 'American Architecture', 'Author', 'Street-Porter', 'Title', "The Los Angeles House "
                    "Decoration and Design in America's 12th-Century City", 'Publisher', 'Potter', 'Shelf', '12',
                    'Category', 'Architecture', 'Subject', 'American Architecture', 'Author', 'Montreal Museum of Fine '
                    'Arts', 'Title', 'Jean-Noël Desmarais Pavilion', 'Publisher', 'Montreal Museum of Fine Arts',
                    'Shelf', '16', 'Category', 'Architecture', 'Subject', 'Design', 'Author', 'Montreal Museum of Fine '
                    'Arts', 'Title', 'Architects for Snoopy', 'Publisher', 'Montreal Museum of Fine Arts', 'Shelf',
                    '26', 'Category', 'Architecture', 'Subject', 'Humour', 'Author', 'Petre and van der Hoek', 'Title',
                    'Software Design Decoded 66 Ways Experts Thinkl', 'Publisher', 'MIT Press', 'Shelf', '35',
                    'Category', 'Programming', 'Subject', 'Engineering']
        actual = search_books(user_search_option, user_search_term)
        self.assertEqual(expected, actual)

    def test_invalid_search_books(self):
        """Test search term not found."""
        user_search_option = "Title"
        user_search_term = "feqr32"
        expected = []
        actual = search_books(user_search_option, user_search_term)
        self.assertEqual(expected, actual)
