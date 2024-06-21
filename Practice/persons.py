import sqlite3
#connect to a (new) database
conn = sqlite3.connect("PycharmProjects/study7")

#create a cursor
cur = conn.cursor()

#create a "people" table
cur.execute("""CREATE TABLE IF NOT EXISTS people
            (first_name TEXT, last_name TEXT)""")
conn.commit()



names_list =[
("Roderick", "Watson"),
 ("Mykyta", "Narozhnyi"),
 ("Julia", ""),
 ("Imagine", "People")
]

cur.executemany('''
    INSERT INTO people (first_name, last_name) VALUES (?,?)
    ''', names_list)
conn.commit()

# Close connection
cur.close()
conn.close()