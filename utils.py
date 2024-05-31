import logging
import datetime
logging.basicConfig(filename='loggingutils.py.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

BOOKS = [
    {
        "name": "Dune",
        "author": "Frank Herbert",
        "genre": "Science fiction",
        "pages": 896,
        "entry_added": datetime.time,
    },
    {
        "name": "Dune Messiah",
        "author": "Frank Herbert",
        "genre": "Science fiction",
        "pages": 256,
        "entry_added": datetime.time,
    },
    {
        "name": "Murder on the Orient Express",
        "author": "Agatha Christie",
        "genre": "Crime novel",
        "pages": 256,
        "entry_added": datetime.time,
    },
]


def exit_menu():
    logger.info("User chosed to exit")
def get_user_input(attr_name):
    value = ''
    while value == '':
        value = input(f"Enter the {attr_name} of the book: ")
    return value

def add_book():
    logger.info("User added a new book")
    author = get_user_input("author")
    name = get_user_input("name")
    genre = get_user_input("genre")
    pages = ''
    while not pages.isdigit():
        pages = get_user_input("pages (number only)")
        if not pages.isdigit():
            print("Please enter a numerical value for pages.")
    pages = int(pages)
    time_added = datetime.datetime.now()
    new_book = {
        "name": name,
        "author": author,
        "genre": genre,
        "pages": pages,
        "entry_added": time_added,
    }
    BOOKS.append(new_book)
    print(f"Book '{new_book['name']}' is successfully added!")

def print_all_books():
    logger.info("User chosed to print all books")
    for book in BOOKS:
        print(f"'{book['name']}' by {book['author']} - Genre: {book['genre']}, Pages: {book['pages']}")
        print('=' * 60)

def random_book_selection():
    logger.info("User chosed a random book")
    if BOOKS:
        book = random.choice(BOOKS)
        print(f"Random book selection: '{book['name']}' by {book['author']}")
    else:
        print("No books in the library.")

def exit_from_menu():
    print('You chose exiting the program.')
    exit_menu()

def books_csv1():
    with open("books.csv", "w") as data_file:
        fields = ["name", "author", "genre", "pages", "entry_added"
                  ]
        # if BOOKS:
        # fieldnames = list(BOOKS[0].keys)
        writer = csv.DictWriter(data_file, fieldnames=fields)
        writer.writeheader()
        for book in BOOKS:
            writer.writerow(book)
