import json
import csv

with open ("books.json", "r") as data_file:
    data = json.load(data_file)

with open("new_books.csv", "w") as csv_file:
    writer = csv.writer(csv_file)
    for new_book in :
        writer.writerow(new_book)