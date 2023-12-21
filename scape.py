import feedparser 
from entry import NewsArticle
from bs4 import BeautifulSoup
from typing import List
from urllib.parse import urljoin
import requests

def article_images(link): 
    page = requests.get(link)
    if page.status_code != 200:
        return []
    
    dom_doc = BeautifulSoup(page.content, 'html.parser')
    bilder_div = dom_doc.find("div", class_="bildergalerie-content")
    a_tags = bilder_div.find_all("a")
    return [urljoin(link, i["href"]) for i in a_tags]

def read_articles() -> List[NewsArticle]:
    news_feed = feedparser.parse("https://schwarzesbrett.bremen.de/sixcms/detail.php?template=01_rss_feed_d&contentId=28555")
    articles = []
    for entry in news_feed.entries:
        articles.append(NewsArticle(
            title = entry["title"],
            id = entry["id"],
            link = entry["link"],
            published = entry["published"],
            summary = entry["summary"]
        ))
    return articles

if __name__ == '__main__':
    articles = read_articles()
    # for article in articles:
    #     article.images = article_images(article.link)

    articles[0].images = article_images(articles[0].link)
    print(articles[0].images)
    
