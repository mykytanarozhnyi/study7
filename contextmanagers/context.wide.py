import json
f"""Написати клас-менеджер контексту,
 який при вході в контекст відкриває файл з іменем,
  переданим йому як аргумент на запис. 
  На виході з контексту відбувається обов'язкове закриття файлу.
Також відбувається перевірка типу помилки,
яка могла відбутися під час роботи всередині контексту: 
якщо відбулася помилка типу IndexError, додається запис логу рівня error
з повідомленням про помилку та це виключення 
помічається як оброблене та не передається далі.
Усі інші типи помилок передаються далі без обробки."""

import json
import csv
from contextlib import contextmanager

class WriteFileContext:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

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