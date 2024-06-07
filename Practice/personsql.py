import sqlite3
from contextlib import closing

def write_to_db(name,age):
    cursor.execute("""
    INSERT INTO person VALUES(:name,:age)
    """, data)


#connection = sqlite3.connect("person.db")
#cursor = connection.cursor()
class Person:

    def __init__(self,_id,name,age,eye_color):
        self.id = _id
        self.name = name
        self.age = age
        self.eye_color = eye_color

if __name__ == "__main__":
    with closing(sqlite3.connect("person.db")) as connection:
        cursor = connection.cursor()
        cursor.execute("""""")
            CREATE TABLE IF NOT EXISTS person(
                id INTEGER PRIMARY KEY,
                name CHAR(30)
                age INTEGER
            )
            """)
        with connection:
            write_to_db(cursor, "Mariia Ivanivna",50)
        cursor.execute("""

        INSERT INTO person VALUES
        (1,"Vasya",15)
        (2,"Petro",80)
        """)
        for person in persons.fetchall():
        print(person)


    if __name__ == "__main__":
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS person(
        id INTEGER,
        name CHAR(30),
        age INTEGER,
        eye_color CHAR(30)
        )
        """)

#    cursor.execute ("""
    #    INSERT INTO person VALUES
        #(1,"Vasya", 15, "yellow"),
        #(2,"Petro", 80, "black")
    #""")
    #connection.commit()
    # після селекту перераховуємо які колонки цікавлять
    #persons = cursor.execute("""
    #    SELECT * FROM person
        """)

#    persons = cursor.execute("""
#    SELECT DISTINCT name FROM person
#    """)

#    unique_names = {person[0] for person in persons.fetchall()}
#    print(unique_names)
 #   for person in persons.fetchall():
 #       print(person)
#    cursor.execute("""
#    ALTER TABLE person
#    ADD PRIMARY KEY (nid)
#    """)
    #cursor.execute("""
    #UPDATE person
    #SET age = 16
    #WHERE name = "Vasya" AND eye_color = "brown"
    #""")
    #connection.commit()
    #persons = cursor.execute("""
    #    SELECT * FROM person
    #    """)
    #for person in persons.fetchall():
    #    print(person)

#cursor.execute("""DROP TABLE person""")
#connection.commit()