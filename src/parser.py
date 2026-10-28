import requests
import re
from bs4 import BeautifulSoup
from src.database import DatabaseRepository

class ForumParser():

    def __init__(self):
        self.repository = DatabaseRepository()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/120.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
        }

    def parse_page(self, url: str):
        r = requests.get(url=url, headers=self.headers)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "lxml")

        items = soup.select("li.comments-feed-item")

        res = []
        id = 0

        for li in items:
            li_id = li.get("id", "")
            comment_uuid = li_id.removeprefix("comment-")

            author_tag = li.select_one("a.threads-text.author")
            author = author_tag.get_text(strip=True) if author_tag else '-'

            body_div = li.find(id=re.compile(r'^existingCommentDiv'))
            text = body_div.get_text(' ', strip=True) if body_div else '-'    

            res.append((id, comment_uuid, author, text))
            id += 1

        self.__save_to_db(res, self.repository)
        
    def __save_to_db(self, parsed_data: list, repository: DatabaseRepository):
        for id, comment_uuid, author, text in parsed_data:
            repository.add(id, comment_uuid, author, text)