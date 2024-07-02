from bs4 import BeautifulSoup
import requests

static_endpoint = "https://appbrewery.github.io/news.ycombinator.com/"

response = requests.get(static_endpoint)
static_page = response.text

soup = BeautifulSoup(static_page, 'html.parser')

article_tag = soup.find_all(name="a", class_="storylink")
article_text = []
article_link = []

for article in article_tag:
    text = article.getText()
    article_text.append(text)
    link = article.get("href")
    article_link.append(link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

highest_score = article_upvote.index(max(article_upvote))

print(article_text[highest_score])
print(article_link[highest_score])
print(article_upvote[highest_score])