from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)

all_anchor = soup.find_all(name="a")
print(all_anchor)

for tag in all_anchor:
    print(tag.getText())
    # Link
    print(tag.get("href"))

h1_heading = soup.find(name="h1", id="name")
print(h1_heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.getText())

# CSS Selectors
company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(".heading")
print(headings)
