from bs4 import BeautifulSoup
import requests

# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)
#
# print(soup.prettify())
# print(soup.a)

# all_anchor_tags = soup.find_all(name="a")
#
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# company_url = soup.select_one(selector="p a")
# print(company_url)

# name = soup.select_one(selector="#name")
# print(name)

# heading = soup.select(".heading")
# print(heading)

url = "https://news.ycombinator.com/news"
response = requests.get(url)
# print(response.text)
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

# first_span = soup.find(name="span", class_="titleline")
# article_tag = first_span.find("a")
# article_text = article_tag.get_text()
# article_link = article_tag.get("href")
# article_upvote = soup.find(name="span", class_="score").get_text()
#
# print(article_link)
# print(article_upvote)

articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []

for tag in articles:
    tag_a = tag.find("a")

    tag_text = tag_a.get_text()
    article_texts.append(tag_text)

    tag_link = tag_a.get("href")
    article_links.append(tag_link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
print(article_texts, article_links, article_upvotes)

highest_vote = max(article_upvotes)
highest_index = article_upvotes.index(highest_vote)
highest_title = article_texts[highest_index]
highest_link = article_links[highest_index]

print(f"The article with the highest upvote is: {highest_title},\n it's link is: {highest_link},\n with a score of: {highest_vote}")
