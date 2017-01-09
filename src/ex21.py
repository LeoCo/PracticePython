import requests
from bs4 import BeautifulSoup


url = 'http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "html.parser")

content = ""

for lines in soup.find_all('p'):
    content += str(lines.getText())


with open('file_to_save.txt', 'w') as open_file:
    open_file.write(content)