import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

news_url = "https://news.google.com/news/rss"
news_open = urlopen(news_url)
xml_page = news_open.read()
news_open.close()

# print(xml_page)
soup_page = soup(xml_page, "xml")
news_list = soup_page.findAll("item")
# print(type(news_list))


# Print news title, url and publish date
i = 1
for news in news_list:
    print(news.title.text)
    print(news.link.text)
    print(news.pubDate.text)
    # print(news.description.text)
    print("-"*60)
    i += 1
    if i == 6:
        break
