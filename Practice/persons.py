import sqlite3
#connect to a (new) database
conn = sqlite3.connect("D:\\demo\\alpha.db")

#create a cursor
cur = conn.cursor()

#create a "people" table
cur.execute("""CREATE TABLE IF NOT EXISTS people
            (first_name TEXT, last_name TEXT)""")
conn.commit()

# Close connection
cur.close()
conn.close()

"Roderick" "Watson"
"Mykyta" "Narozhnyi"
"Julia"
