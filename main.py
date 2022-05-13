from util.database import DatabaseHandler
import os
from dotenv import load_dotenv
from pathlib import Path


class TelegramBot(object):
    def __init__(self, db_name):
        self.db = DatabaseHandler(db_name)
        self.db.setup()


def load_dotenv_resource():
    dotenv_path = Path('.env')
    load_dotenv(dotenv_path=dotenv_path)


if __name__ == '__main__':
    load_dotenv_resource()
    db_file = os.getenv("DB_FILE")

    TelegramBot(db_name=db_file)