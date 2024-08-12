import os
from PySide6 import QtSql
from PySide6 import QtCore
import sqlite3

class Data(QtCore.QObject):
    def __init__(self):
        super(Data, self).__init__()
        print("---<<< CREATE initalise sqlite3 CONNECTION >>>---")
        DATABASE = 'books.db'
        if os.path.isfile(DATABASE) is False:
            print("--->>>---DATABASE IS FALSE SO GOING TO CREATE ONE---<<<---")
            with sqlite3.connect('books.db') as conn:
                cur = conn.cursor()
                cur.execute(
                    """CREATE TABLE IF NOT EXISTS booksdb (ID integer primary key AUTOINCREMENT, Title VARCHAR(20), Price INT, Quantity INT, UPC VARCHAR(30), Product VARCHAR(30), Availability VARCHAR(30), URL VARCHAR)""")
                conn.commit()
        else:
            print("DATABASE ALREADY EXISTS")

        self.create_connection()

    def create_connection(self):
        print("---<<< CREATING CONNECTION >>>---")
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('books.db')

    def delete_selectedids(self, idlist):
        print("DELETE SELECTEDID ON THE sqlConnection")
        for id in idlist:
            with sqlite3.connect('books.db') as self.con:
                self.cur = self.con.cursor()
                self.cur.execute(f"DELETE FROM booksdb WHERE id = {id}")
                self.con.commit()
                print(f"Record {id} deleted successfully")
            self.cur.close()
        return True



    def close_connection(self):
        if self.db.open():
            print("CONNECTION TO DATABASE NEEDS TO BE CLOSED is this a error ?")
            self.db.close()