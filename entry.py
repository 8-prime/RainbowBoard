import datetime
import json
from typing import List


class Rental:
    def __init__(self, title: str = None, summary: str = None, published: datetime = None, 
                link: str = None, id: int = None, images: List[str] = None, name: str = None, 
                cold_rent: str = None, warm_rent: str = None, area: str = None, text: str = None):
        self.title = title
        self.summary = summary
        self.published = published
        self.link = link
        self.id = id
        self.images = images
        self.name = name
        self.cold_rent = cold_rent
        self.warm_rent = warm_rent
        self.area = area
        self.text = text

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)