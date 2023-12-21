import feedparser 
from entry import Rental
from bs4 import BeautifulSoup
from typing import List
from urllib.parse import urljoin
import requests
import re
import json


def soup_images(soup, base_href):
    bilder_div = soup.find("div", class_="bildergalerie-content")
    if(not bilder_div):
        return []
    a_tags = bilder_div.find_all("a")
    return [urljoin(base_href, i["href"]) for i in a_tags]

def soup_cold_rent(article_text) -> str:
    match = re.search(r"(?P<rent>\d+)€(?P<unit>kalt)", article_text)

    if match:
        return match.group("rent")
    else:
        return ""

def soup_warm_rent(article_text) -> str:
    match = re.search(r"(?P<rent>\d+)€(?P<unit>warm)", article_text)

    if match:
        return match.group("rent")
    else:
        return ""

def soup_area(article_text) -> str:
    
    match_qm = re.search(r"(?P<square_meters>\d+)\s*qm", article_text)
    match_m2 = re.search(r"(?P<square_meters>\d+)\s*m²", article_text)
    match_qm2 = re.search(r"(?P<square_meters>\d+)\s*quadratmeter", article_text)

    # If a match is found for qm or m², return the square meters
    if match_qm:
        return match_qm.group("square_meters")
    elif match_m2:
        return match_m2.group("square_meters")
    elif match_qm2:
        return match_qm2.group("square_meters")
    return ""



def soup_article(article: Rental): 
    page = requests.get(article.link)
    if page.status_code != 200:
        return []
    
    soup = BeautifulSoup(page.content, 'html.parser')
    article.name = soup.find("p", class_="entry_name").text
    article.text = "\n".join([x.text for x in soup.findAll("p", class_="entry_text")])

    article.images = soup_images(soup, article.link)

    parseable_text = article.text.lower()
    article.cold_rent = soup_cold_rent(parseable_text)
    article.warm_rent = soup_warm_rent(parseable_text)
    article.area = soup_area(parseable_text)

    

def read_articles() -> List[Rental]:
    news_feed = feedparser.parse("https://schwarzesbrett.bremen.de/sixcms/detail.php?template=01_rss_feed_d&contentId=28555")
    articles = []
    for entry in news_feed.entries:
        articles.append(Rental(
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


    for i in range(5):
        soup_article(articles[i])
        with open("data{num}.json".format(num = i), "w", encoding="utf-8") as file:
            file.write(articles[i].to_json())



    
