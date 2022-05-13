import sqlite3


class DatabaseHandler(object):
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)

    def setup(self):
        stmt = "CREATE TABLE IF NOT EXISTS items (description text)"
        self.conn.execute(stmt)
        self.conn.commit()
