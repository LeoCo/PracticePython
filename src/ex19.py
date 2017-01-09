import requests
from bs4 import BeautifulSoup


url = 'http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "html.parser")

for lines in soup.find_all('p'):
    print(str(lines.getText()))
