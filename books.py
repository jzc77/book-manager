"""
Book collection manager.
"""

import doctest


def START_MESSAGE() -> None:
    """
    Print the welcome message for the user.

    :post-condition: print the welcome message as a string
    """
    separator = "+++++++ " * 8
    print(f"\n{separator}")
    print(f"\nHello, I am excited to see you again!")
    print(f"As always, as your personal book manager, I am at your service.")
    print(f"Please let me know below how I can help you today.\n")
    print(f"{separator}")


def MAIN_MENU() -> None:
    """
    Print the menu for the user.

    :post-condition: print instructions as a string
    """
    print(f"\nEnter 1 to search by author.")
    print(f"Enter 2 to search by title.")
    print(f"Enter 3 to search by publisher.")
    print(f"Enter 4 to search by shelf.")
    print(f"Enter 5 to search by category.")
    print(f"Enter 6 to search by subject.")
    print(f"Enter 7 to quit the program.\n")


def MOVE_OR_QUIT_MENU() -> None:
    """
    Print the secondary menu for the user after searching for a book.

    :post-condition: print instructions as a string
    """
    print(text_separator(65))
    print(f"Your results are displayed above! What would you like to do next?")
    print(text_separator(65))
    print(f"\nEnter 1 to move a book.")
    print(f"Enter 2 to quit the program.\n")


def SHELF_MENU() -> None:
    """
    Print the shelf menu for the user.

    This function will print the instructions on where to move a chosen book. The integers 1 to 38 represents
    Shelves 1 to 38. Integers 39 to 44 represents the non-integer shelf names (Gaby, Island, Lego, Noguchi, Reading,
    and Students).

    :post-condition: print instructions as a string
    """
    print(f"\n{text_separator(40)}")
    print(f"Where do you want to move this book to?")
    print(text_separator(40))
    print(f"\nTo move to any of your 38 shelves (wow!), enter a number from 1 to 38.")
    print(f"Enter 39 to move this book to Gaby.")
    print(f"Enter 40 to move this book to Island.")
    print(f"Enter 41 to move this book to Lego.")
    print(f"Enter 42 to move this book to Noguchi.")
    print(f"Enter 43 to move this book to Reading.")
    print(f"Enter 44 to move this book to Students." "\n")


def text_separator(number_of_dashes: int) -> str:
    """
    Separate text with dashes.

    :param: the specified number of dashes needed
    :precondition: a positive integer
    :post-condition: a string of dashes
    :return: the number of dashes specified by input

    >>> text_separator(12)
    '------------'
    >>> text_separator(1)
    '-'
    >>> text_separator(0)
    ''
    """
    separator = "-" * number_of_dashes
    return separator


def get_book_information(book_text_file) -> tuple:
    """
    Store each book as a dictionary and place the dictionaries into a tuple.

    Make a tuple of dictionaries:
    Read first line and make into keys (Author, Title etc) by searching with number of tab spaces.
    Make a dictionary with the headers and put the dictionaries into a list.
    Convert the list of dictionaries into a tuple of dictionaries.

    :precondition: a .txt file is present in the same folder as this Python file.
    :precondition: the .txt file has columns for Author, Title, Publisher, Shelf, Category, and Subject separated
                   by tabs
    :return: tuple filled with dictionaries of books
    """
    text_file = book_text_file
    with open(text_file, encoding="UTF-8") as file_object:
        all_lines = []
        for line in file_object:
            split_lines = check_format(line)
            if '' in split_lines:
                split_lines[2] = "None"
            all_lines.append(split_lines)

        header_keys = all_lines[0]

        list_of_dictionaries = []
        for single_line in all_lines[1:]:
            zip_header_keys_and_values = zip(header_keys, single_line)  # Zipping two lists, which gives a zipped object
            individual_dictionaries = dict(zip_header_keys_and_values)
            list_of_dictionaries.append(individual_dictionaries)
        tuple_of_dictionaries = tuple(list_of_dictionaries)

        return tuple_of_dictionaries


def check_format(line: str) -> list:
    """
    Check format of file to see if the entries are stripped and split by tab correctly.

    :param: a line of the text file
    :precondition: the line is a string
    :post-condition: the line is put into a list
    :return: the line is returned as a list

    >>> check_format("Dupre	Skyscrapers	BD&L	12	Architecture	20th Century")
    ['Dupre     Skyscrapers     BD&L    12      Architecture    20th Century']
    >>> check_format("Dupre	Skyscrapers	BD&L	12	Architecture	20th Century"\
    "Hollingsworth	Architecture of the 20th Century	Exeter	6	Architecture	20th Century")
    ['Dupre     Skyscrapers     BD&L    12      Architecture    20th CenturyHollingsworth Architecture of the 20th\
 Century        Exeter  6       Architecture    20th Century']
    >>> check_format("")
    ['']
    """
    split_lines = line.strip().split('\t')
    return split_lines


def search_option() -> str:
    """
    Validate user input.

    :precondition: user inputs an integer between 1 and 7 inclusively
    :post-condition: user input as a string
    :return: user's search by input as a string
    """
    valid_input = ["1", "2", "3", "4", "5", "6", "7"]

    search_option_list = ["Author", "Title", "Publisher", "Shelf", "Category", "Subject"]

    while True:
        user_input = input(f"Your input: ")
        if user_input not in valid_input:
            print(f"\nPlease enter a valid response between 1 to 7, inclusively.")
            continue
        if user_input == "7":
            return "quit"
        else:
            search_option_index = int(user_input)
            search_by_option = search_option_list[search_option_index - 1]
            return search_by_option  # return search option by name


def get_valid_move_or_quit_input() -> str:
    """
    Validate user input.

    :precondition: user inputs an integer between 1 and 2 inclusively
    :post-condition: user input as a string
    :return: user input as a string
    """
    valid_input = ["1", "2"]
    while True:
        user_input = input(f"Your input: ")
        if user_input not in valid_input:
            print("Please enter a valid response between 1 to 2, inclusively.")
            continue
        if user_input == "2":
            return "quit"
        else:
            return user_input


def search_term() -> str:
    """
    Obtain user's search term.

    :precondition: a string of characters
    :post-condition: a string of characters
    :return: user's search term as a string
    """
    user_search_term = input(f"Awesome! Please enter your search term: ")
    return user_search_term


def search_books(user_search_option: str, user_search_term: str) -> list:
    """
    Search the collection of books by author, title, publisher, shelf, category, or subject.

    :pre-condition: any combination of letters
    :post-condition: list of results of all authors, title, publisher, shelf, category, or subject that matches the
                     search query
    :return: list of matching books searched by either author, title, publisher, shelf, category, or subject
    >>> search_books("Title", "feqr32")
    <BLANKLINE>
    0 results found.
    <BLANKLINE>
    []
    >>> search_books("Author", "tre") # doctest: +NORMALIZE_WHITESPACE
    <BLANKLINE>
    5 results found.
    <BLANKLINE>
    Result 1
    ---------
    Author: Longstreth
    Title: On the Edge of the World Four Architects in SF at the Turn of the Century
    Publisher: University of California Press
    Shelf: 5
    Category: Architecture
    Subject: American Architecture
    <BLANKLINE>
    Result 2
    ---------
    Author: Street-Porter
    Title: The Los Angeles House Decoration and Design in America's 12th-Century City
    Publisher: Potter
    Shelf: 12
    Category: Architecture
    Subject: American Architecture
    <BLANKLINE>
    Result 3
    ---------
    Author: Montreal Museum of Fine Arts
    Title: Jean-Noël Desmarais Pavilion
    Publisher: Montreal Museum of Fine Arts
    Shelf: 16
    Category: Architecture
    Subject: Design
    <BLANKLINE>
    Result 4
    ---------
    Author: Montreal Museum of Fine Arts
    Title: Architects for Snoopy
    Publisher: Montreal Museum of Fine Arts
    Shelf: 26
    Category: Architecture
    Subject: Humour
    <BLANKLINE>
    Result 5
    ---------
    Author: Petre and van der Hoek
    Title: Software Design Decoded 66 Ways Experts Thinkl
    Publisher: MIT Press
    Shelf: 35
    Category: Programming
    Subject: Engineering
    <BLANKLINE>
    ['Author', 'Longstreth', 'Title', 'On the Edge of the World Four Architects in SF at the Turn of the Century',\
    'Publisher', 'University of California Press', 'Shelf', '5', 'Category', 'Architecture', 'Subject', 'American\
    Architecture', 'Author', 'Street-Porter', 'Title', "The Los Angeles House Decoration and Design in America's\
    12th-Century City", 'Publisher', 'Potter', 'Shelf', '12', 'Category', 'Architecture', 'Subject', 'American\
    Architecture', 'Author', 'Montreal Museum of Fine Arts', 'Title', 'Jean-Noël Desmarais Pavilion', 'Publisher',\
    'Montreal Museum of Fine Arts', 'Shelf', '16', 'Category', 'Architecture', 'Subject', 'Design', 'Author', 'Montreal\
    Museum of Fine Arts', 'Title', 'Architects for Snoopy', 'Publisher', 'Montreal Museum of Fine Arts', 'Shelf',\
    '26', 'Category', 'Architecture', 'Subject', 'Humour', 'Author', 'Petre and van der Hoek', 'Title', 'Software\
    Design Decoded 66 Ways Experts Thinkl', 'Publisher', 'MIT Press', 'Shelf', '35', 'Category', 'Programming',\
        'Subject', 'Engineering']
    """
    book_collection = get_book_information("Books UTF-16.txt")
    all_book_matches = [book[user_search_option] for book in book_collection if user_search_option in book]
    valid_results = [option for option in all_book_matches if user_search_term in option]
    result_count = f"\n{len(valid_results)} results found."
    print(result_count, end="\n\n")

    matched_books = []
    for book in book_collection:
        option = book[user_search_option]
        if option in valid_results:
            matched_books.append(book)

    book_counter = 0
    matching_books = []
    for book in matched_books:
        book_counter += 1
        print(f"Result {book_counter} \n{text_separator(9)}")
        for key, value in book.items():
            matching_books.append(key)
            matching_books.append(value)
            print(f"{key}: {value}")
        print(end="\n")
    return matching_books


def validate_and_obtain_shelf_destination() -> str:
    """
    Validate user input.

    This function will match the user's input of the integers between 1 and 44 to the shelf name. Integers 1 to 38
    represents Shelves 1 to 38. Integers 39 to 44 represents the non-integer shelf names (Gaby, Island, Lego, Noguchi,
    Reading, and Students).

    :precondition: user inputs an integer between 1 and 44 inclusively
    :post-condition: a match of the user input to shelf name as a string
    :return: a match of the user input to shelf name as a string
    """
    valid_range = range(1, 45)
    valid_input = []
    [valid_input.append(str(integer)) for integer in valid_range]

    return_range = range(1, 39)
    search_option_list = ["Gaby", "Island", "Lego", "Noguchi", "Reading", "Students"]
    return_list = []
    [return_list.append(str(integer)) for integer in return_range]
    [return_list.append(search_selection) for search_selection in search_option_list]

    while True:
        user_input = input(f"Your input: ")
        if user_input not in valid_input:
            print(f"\nPlease enter a valid response between 1 to 44, inclusively.")
            continue
        else:
            search_option_index = int(user_input)
            shelf_option_return = return_list[search_option_index - 1]
            return shelf_option_return
            #  Will return one of '1', '2'...'38', 'Gaby', 'Island', 'Lego', 'Noguchi', 'Reading', 'Students'


def obtain_book_to_move() -> str:
    """
    Obtain book result number for subsequent moving.

    This function will have the user select the result number of a book they want to move instead of typing the title,
    author, publisher etc. This will minimize typing errors and will provide a more efficient method for the user
    to select a book.

    :precondition: positive integer
    :post-condition: a positive integer as a string
    :return: user's search term as a string
    """
    print(f"\n{text_separator(77)}")
    print(f"From the results above, type the result number of the book you want to move.")
    print(f"For example, to move book Result 1, type 1.")
    print(text_separator(77))
    while True:
        book_result_number = input(f"\nPlease enter the book result number here: ")
        try:
            return str(int(book_result_number))
        except ValueError:
            print(f"\nPlease enter a positive integer.")
            continue


def move_book(matched_books: list, book_result_to_move: str, shelf_to_move_to: str) -> tuple:
    """
    Move a specified book from one shelf to another.

    The book will be moved by obtaining the book's shelf value and replacing it with the user-specified value.

    :param: a list of matched books searched by a specific query
    :param: a string of an integer representing the book result to move
    :param: a string of an integer or shelf name representing the shelf to move the book to
    :precondition: a list of matched book searched by a specific query
    :precondition: a string of an integer
    :precondition: a string of an integer or shelf name
    :post-condition: selects a specified book from the matched books list and find it in the tuple of dictionaries
                     of books. The specified book's shelf number will be modified to the specified shelf name.
    :return: a dictionary of updated book shelf information
    """
    book_collection = get_book_information("Books UTF-16.txt")

    matched_book_position = ((int(book_result_to_move) - 1) * 12)  # Will obtain "Author" in the matched_books list
    one_matched_book_slice = slice(matched_book_position, matched_book_position + 12)

    one_matched_book_list = matched_books[one_matched_book_slice]  # One book only as a list: ['Author', 'Tzonis', ...]
    if not one_matched_book_list:
        print(f"\n{text_separator(83)}\nBook result not found. You may have typed out of range. Please try searching "
              f"again.\n{text_separator(83)}")
        return book_collection
    else:
        for book in book_collection:
            if one_matched_book_list[1] == book["Author"] and one_matched_book_list[3] == book["Title"] and \
                    one_matched_book_list[5] == book["Publisher"] and one_matched_book_list[7] == book["Shelf"] and \
                    one_matched_book_list[9] == book["Category"] and one_matched_book_list[11] == book["Subject"]:
                book["Shelf"] = shelf_to_move_to
        print(f"\n{text_separator(123)}\nOk! I will move the book titled '{one_matched_book_list[3]}' on Shelf "
              f"{one_matched_book_list[7]} to Shelf {shelf_to_move_to}, when you quit the program.")
        print(f"What would you like to do next?")
        print(text_separator(123))
        return book_collection


def quit_program(moved_books: tuple) -> None:  # A tuple of updated dictionaries passed in as parameters
    """
    Create a new text file and replace existing file with new book information.

    This function will replace the existing .txt file with updated information if the user decides to move a book.
    The headers of the file will be printed to the file first and the individual values of the updated dictionaries
    will be sequentially added to the new file. The function will also print a confirmation message that the file
    (or "bookshelf") has been updated

    :param: moved books
    :precondition: a tuple of updated dictionaries of books searched by a specific query
    :post-condition: create a new .txt file that has the updated information of the existing file
    """
    new_file = "Books UTF-16.txt"
    with open(new_file, 'w',  encoding="UTF-8") as file_object:
        file_object.write(f"Author\tTitle\tPublisher\tShelf\tCategory\tSubject\n")

        try:
            for book in moved_books:
                book_values = [value for value in book.values()]
                formatted_line = format_quit_file(book_values)
                file_object.write(f"{formatted_line}\n")
            print(f"\n{text_separator(91)}")
            print(f"Alrighty then; I'll see you soon! Your bookshelf has been updated if you have moved a book.")
            print(text_separator(91))

        except TypeError:
            print(f"No books moved.")


def format_quit_file(book_values: list) -> str:
    """
    Format the file on quit.

    :param: a line of the text file
    :precondition: the line is a string
    :post-condition: the line is put into a list
    :return: the line is returned as a list

    >>> format_quit_file(["Dupre", "Skyscrapers", "BD&L", "Gaby", "Architecture", "20th Century", "Hollingsworth",\
    "Architecture of the 20th Century", "Exeter", "6", "Architecture", "20th Century"])
    'Dupre\\tSkyscrapers\\tBD&L\\tGaby\\tArchitecture\\t20th Century\\tHollingsworth\\tArchitecture of the 20th Century\
\\tExeter\\t6\\tArchitecture\\t20th Century'
    >>> format_quit_file(["Author", "Dupre"])
    'Author\\tDupre'
    >>> format_quit_file([])
    ''
    """
    formatted_line = '\t'.join(book_values)
    return formatted_line


def books() -> None:
    """Run book program.

    This function will run all the other functions in the program. If the quit function is selected, the loop will end.
    """
    START_MESSAGE()
    updated_books = get_book_information("Books UTF-16.txt")
    status = True
    while status:
        MAIN_MENU()  # 6 search options and quit
        user_search_option = search_option()
        if user_search_option == "quit":
            break
        else:
            user_search_term = search_term()
            matched_books = search_books(user_search_option, user_search_term)  # Gives a list
            MOVE_OR_QUIT_MENU()  # Next menu printed
            user_move_or_quit_option = get_valid_move_or_quit_input()
            if user_move_or_quit_option == "quit":
                break
            else:
                if not matched_books:
                    print(f"\n{text_separator(65)}")
                    print(f"I'm very sorry! No results were found. Please try searching again.")
                    print(text_separator(65))
                else:
                    book_result_to_move = obtain_book_to_move()  # Makes user select the result number
                    SHELF_MENU()
                    shelf_to_move_to = validate_and_obtain_shelf_destination()  # Ask for what shelf to move to
                    updated_books = move_book(matched_books, book_result_to_move, shelf_to_move_to)
    quit_program(updated_books)


def main() -> None:
    """
    Drives the program.
    """
    doctest.testmod()
    books()


if __name__ == "__main__":
    main()
