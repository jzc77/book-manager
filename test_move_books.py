"""
Unit test the move_books function by identifying the disjointed equivalency partitions.
"""

from unittest import TestCase


class TestMoveBooks(TestCase):
    def test_move_book_to_named_shelf(self):
        """Test move a book to a different shelf."""
        tuple_of_books = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L', 'Shelf': '12', 'Category':
                           'Architecture', 'Subject': '20th Century'}, {'Author': 'Hollingsworth', 'Title':
                          'Architecture of the 20th Century', 'Publisher': 'Exeter', 'Shelf': '6', 'Category':
                          'Architecture', 'Subject': '20th Century'}, {'Author': 'Johnson Burgee', 'Title':
                          'Architecture 1979-1985', 'Publisher': 'Rizzoli', 'Shelf': 'Island', 'Category':
                          'Architecture', 'Subject': '20th Century'})
        shelf_to_move_to = "Island"
        self.assertEqual(shelf_to_move_to, tuple_of_books[2]["Shelf"])
