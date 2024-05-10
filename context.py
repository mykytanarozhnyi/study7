import json
import csv
class WriteFileContext:
    def __init__(self,filename):
        self.filename = "books.json"

    def __enter__(self):
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self, type, value, traceback):
        if type:
            print(traceback)
        self.file.close()
        #return True

if __name__ == "__main__":

    with open("books.json", "r") as json_file, open ("books.csv", "w") as csv_file:
        data = json.load(json_file)
        writer = csv.writer(csv.file)
        for book in data:
            writer.writerow(book)

    with WriteFileContext("filename.txt") as outfile:
        outfile.write("Example text")
        raise IndexError()

    print(outfile.closed)