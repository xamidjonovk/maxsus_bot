import sqlite3


def update_db(first_name, last_name, directory, phone_number, username, user_id):
    try:
        con = sqlite3.connect('students.db')
        cursor = con.cursor()
        print("Connected to SQLite")

        query = """ INSERT INTO students (first_name, last_name, directory, phone_number, username, user_id) 
                    VALUES (?, ?, ?, ?, ?, ?) """

        data = (first_name, last_name, directory, phone_number, username, user_id)

        cursor.execute(query, data)
        con.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)

    finally:
        con.close()
        print("the sqlite connection is closed")
