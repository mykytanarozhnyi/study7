import json
import csv
from contextlib import contextmanager
class WriteFileContext:
    def __init__(self,name):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        #return True

#def write_file_context(filename):
#    file = open(filename,"w")
#    try:
#        yield file
#    except Exception as error:

#    finally:
#        file.close

 if exc_type is not None and issubclass(exc_type, IndexError):

with open('error_log.txt', 'a') as log_file:
                log_file.write(f'Error: {exc_val}\n')
            return True

if __name__ == '__main__':
    try:
        with WriteFileContext('books.json') as file:
            file.write('Some data\n')
    except Exception as e:
        print(f'Error: {e}')


    #with open("books.json", "r") as json_file, open ("books.csv", "w") as csv_file:
    #    data = json.load(json_file)
    #    writer = csv.writer(csv.file)
   #    for book in data:
    #        writer.writerow(book)

    #with WriteFileContext("filename.txt") as outfile:
    #    outfile.write("Example text")
    #    raise IndexError()

    #print(outfile.closed)