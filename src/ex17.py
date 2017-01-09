import requests
from bs4 import BeautifulSoup


url = 'http://www.nytimes.com'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "html.parser")

#print(soup.prettify())

title = soup.find_all(class_="story-heading")

for story_heading in soup.find_all(class_="story-heading"):
    if story_heading.a:
        print(story_heading.a.text.replace("\n", " ").strip())
    else:
        print(story_heading.contents[0].strip())