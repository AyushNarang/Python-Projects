from bs4 import BeautifulSoup
import requests

live_endpoint = "https://news.ycombinator.com/news"

response = requests.get(live_endpoint)
live_page = response.text

soup = BeautifulSoup(live_page, 'html.parser')

articles = soup.find_all(name='span', class_='titleline')
article_text = []
article_link = []
for article in articles:
    text = article.getText()
    article_text.append(text)
    link = article.find(name='a').get('href')
    article_link.append(link)

subtexts = soup.find_all(class_="subtext")

article_upvotes = [int(line.span.span.getText().split()[0]) if line.span.span else 0 for line in soup.find_all(class_='subtext')]

highest_score = article_upvotes.index(max(article_upvotes))

print(article_text[highest_score])
print(article_link[highest_score])
print(article_upvotes[highest_score])