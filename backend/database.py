from pymongo import MongoClient
from dotenv import load_dotenv
import os


load_dotenv()
CONNECTION_STRING = os.getenv('CONNECTION_STRING')
DB_NAME = os.getenv('DB_NAME')


class Database:
    def __init__(self):
        self.db = self.get_db()
        self.datasets = self.db['datasets']

    def get_db(self):
        client = MongoClient(CONNECTION_STRING)
        return client[DB_NAME]

    def get_collection(self, filter_dict={}):
        filter_criteria = {f'tags.{field}': {'$all': values} for field, values in filter_dict['tags'].items()}
        print(filter_criteria)
        return self.datasets.find(filter_criteria)
