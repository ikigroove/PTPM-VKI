import re
from src.database import DatabaseRepository
from src.loader import PageLoader

class ForumParser():

    def __init__(self, repository: DatabaseRepository, loader: PageLoader):
        self.repository = repository
        self.loader = loader

    def parse_page(self, url: str):

        soup = self.loader.get_page(url)

        items = soup.select("li.comments-feed-item")

        res = []
        id = 1

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

        return res
        
    def __save_to_db(self, parsed_data: list, repository: DatabaseRepository):
        for id, comment_uuid, author, text in parsed_data:
            repository.add(id, comment_uuid, author, text)