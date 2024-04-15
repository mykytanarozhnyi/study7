from datetime import datetime
import json

BOOKS = [
    {
        "name": "Dune",
        "author": "Frank Herbert",
        "genre": "Science fiction",
        "pages": 896,
        "entry_added": datetime.now(),
    },
    {
        "name": "Dune Messiah",
        "author": "Frank Herbert",
        "genre": "Science fiction",
        "pages": 256,
        "entry_added": datetime.now(),
    },
    {
        "name": "Murder on the Orient Express",
        "author": "Agatha Christie",
        "genre": "Crime novel",
        "pages": 256,
        "entry_added": datetime.now(),
    },
]
def convert_books_json():
    for book in BOOKS:
        book["entry_added"] = book["entry_added"].timestamp()

    with open("books.json","w") as data_file:
        json.dump(BOOKS, data_file, skipkeys=True, indent=3)


if __name__ == "__main__":
    convert_books_json()
