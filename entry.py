import datetime
from typing import List

class NewsArticle:
    def __init__(self, title: str = None, summary: str = None, published: datetime = None, link: str = None, id: int = None, images: List[str] = None, name: str = None):
        self.title = title
        self.summary = summary
        self.published = published
        self.link = link
        self.id = id
        self.images = images
        self.name = name