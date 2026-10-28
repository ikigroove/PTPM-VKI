import requests
from src.database import DatabaseRepository

class ForumParser():
    def __init__(self):
        self.repository = DatabaseRepository()
        
        pass

    def parse_page(self, url: str):
        pass

    def save_to_db(self, parsed_data, repository):
        pass